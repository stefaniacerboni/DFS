WHITE = 0
GRAY = 1
BLACK = -1
global time


def DFS(G):
    global pile
    pile = []
    for node in G.V:
        node.color = WHITE
        node.pi = None
    global time
    time = 0
    for node in G.V:
        if node.color is WHITE:
            DFS_Visit(G, node)

def DFS_Visit(G, node):
    global time
    time += 1
    node.d = time
    node.color = GRAY
    for adj in node.adj:
        if adj.color is WHITE:
            adj.pi = node
            DFS_Visit(G, adj)
    node.color = BLACK
    time += 1
    node.f = time
    global pile
    pile.insert(0, node.key)

def SCC(Gt, sccList):
    listindex = [0 for i in range(0, len(Gt.V))]

    global pile
    for i in pile:
        listindex[i] = pile[i]
    for node in Gt.V:
        node.color = WHITE
        node.pi = None
    global time
    time = 0
    for index in listindex:
        if(Gt.V[index].color is WHITE):
            sccList[index].append(Gt.V[index].key)
            DFS_Visit_SCC(Gt, Gt.V[index], sccList[index])


def DFS_Visit_SCC(G, node, sccList):
    global time
    time += 1
    node.d = time
    node.color = GRAY
    for adj in node.adj:
        if adj.color is WHITE:
            adj.pi = node
            DFS_Visit_SCC(G, adj, sccList)
        else:
            prec = node
            while prec is not None and prec.key not in sccList:
                sccList.append(prec.key)
                prec = prec.pi
    node.color = BLACK
    time += 1
    node.f = time
