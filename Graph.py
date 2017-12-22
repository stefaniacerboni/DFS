class Node:

    def __init__(self, key):
        self.pi = 0
        self.d = 0
        self.f = 0
        self.color = 0
        self.key = key
        self.adj = []

    def setKey(self, value):
        self.key = value

    def addAdj(self, node):
        self.adj.append(node)


class Arch:
    def __init__(self, u, v):
        self.u = u
        self.v = v


class Graph:
    def __init__(self, nodes, arches):
        self.V = nodes
        self.E = arches