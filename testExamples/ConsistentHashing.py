import hashlib
import bisect


class Node(object):
    """
    Server Node
    capacity would be treated as virtual nodes on ring
    """

    def __init__(self, hostname, port, capacity):
        self.hostname = hostname
        self.port = port
        self.capacity = capacity

    def __cmp__(self, rhs):
        return cmp((hostname, port), (rhs.hostname, rhs.port))

    def __repr__(self):
        """ return node info with 'hostname:port|cap' """
        return '%s:%d|%d' % (self.hostname, self.port, self.capacity)


class ConsistentHashRing(object):
    def __init__(self, replication=3):
        self.hash = hashlib.sha1
        self.ring = dict()
        self._nodeKeys = []
        self.capacityMap = dict()  # reverse capacity query
        self.replication = replication

    def addNode(self, node):
        """
        insert node onto ring with KEY="${nodeString}-${vnodeNumber}"
        """
        self.capacityMap[(node.hostname, node.port)] = node.capacity
        for i in range(0, node.capacity):
            pos = self.generatePosition("%s-%d" % (node, i))
            if pos in self.ring:
                continue
            self.ring[pos] = node
            bisect.insort(self._nodeKeys, pos)

    def removeNode(self, host, port):
        """
        remove a node from ring
        """
        capacity = self.capacityMap[(host, port)]
        for i in range(0, capacity):
            pos = self.generatePosition("%s-%d" % (Node(host, port, capacity), i))
            del self.ring[pos]
            self._nodeKeys.remove(pos)

    def resolveNode(self, key):
        """
        resolve node position from a key
        """
        if not self.ring:
            raise IndexError("Empty ring")

        pos = self.generatePosition(key)
        node = bisect.bisect_right(self._nodeKeys, pos)
        try:
            result = [self.ring[self._nodeKeys[(node + x) % len(self._nodeKeys)]]
                      for x in range(0, self.replication)]
        except IndexError:
            result = self.ring.values()[:self.replication]

        return list(set(result))  # uniquify

    def generatePosition(self, key):
        """
        Get a string key and return a long integer as position in hash ring
        """
        return long(self.hash(key).hexdigest(), 16)
