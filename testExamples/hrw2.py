from collections import defaultdict

from . import murmur3


class RendezvousHash(object):

    def __init__(self, nodes=None, seed=0):
        self.nodes = []
        self.seed = seed
        if nodes is not None:
            self.nodes = nodes
        self.hash_function = lambda x: murmur3.murmur3_32(x, seed)

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.append(node)

    def remove_node(self, node):
        if node in self.nodes:
            self.nodes.remove(node)
        else:
            raise ValueError("No such node %s to remove" % (node))

    def find_node(self, key):
        high_score = -1
        winner = None
        for node in self.nodes:
            score = self.hash_function("%s-%s" % (str(node), str(key)))
            if score > high_score:
                (high_score, winner) = (score, node)
            elif score == high_score:
                (high_score, winner) = (score, max(str(node), str(winner)))
        return winner


