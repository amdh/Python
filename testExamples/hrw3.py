import mmh3
import socket
import struct


def ip2long(ip):
    """Convert an IP string to long."""
    packedIP = socket.inet_aton(ip)
    return struct.unpack("!L", packedIP)[0]


def murmur(key):
    """Return murmur3 hash of the key as 32 bit signed int."""
    return mmh3.hash(key)


def weight(node, key):
    """Return the weight for the key on node.
    Uses the weighing algorithm as prescibed in the original HRW white paper.
    @params:
        node : 32 bit signed int representing IP of the node.
        key : string to be hashed.
    """
    a = 1103515245
    b = 12345
    hash = murmur(key)
    #print hash
    return (a * ((a * node + b) ^ hash) + b) % (2^31)


class Ring(object):
    """A ring of nodes supporting rendezvous hashing based node selection."""
    def __init__(self, nodes=None):
        nodes = nodes or {}
        self._nodes = set(nodes)

    def add(self, node):
        self._nodes.add(node)

    def nodes(self):
        return self._nodes

    def remove(self, node):
        self._nodes.remove(node)

    def hash(self, key):
        """Return the node to which the given key hashes to."""
        assert len(self._nodes) > 0
        weights = []
        for node in self._nodes:
            n = ip2long(node)
            w = weight(n, key)
            #print w
            weights.append((w, node))

        _, node = max(weights)
        return node


# ---------- TEST CODE -----------
ip1 = '1.1.1.1'
ip2 = '2.1.1.2'
ip3 = '3.2.2.2'

ring = Ring()

assert set() == ring.nodes()

ring.add(ip1)
ring.add(ip2)
ring.add(ip3)

print ring.hash(str(101))
print ring.hash(str(120))
print ring.hash(str(11))
print ring.hash(str(12))
print ring.hash(str(13))
print ring.hash(str(531))
print ring.hash(str(1111))
print ring.hash(str(145))
print ring.hash(str(9))
