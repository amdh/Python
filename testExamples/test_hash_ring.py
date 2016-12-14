from hasg_ring import HashRing

def test():
    memcache_servers = ['192.168.0.246:11212',
                        '192.168.0.247:11212',
                        '192.168.0.249:11212']
    ring = HashRing(memcache_servers)
    print ring
    for i in xrange(11, 21):
        server = ring.get_node(str(i))
        print server


test()