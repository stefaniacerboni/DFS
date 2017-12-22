import Graph
import DFS
def test(matrix):
    V = [Graph.Node(i) for i in range(0, len(matrix))]
    E = [[] for i in range(0, len(matrix))]
    G = Graph.Graph(V,E)
    Et = [[] for i in range(0, len(matrix))]
    Vt = [Graph.Node(i) for i in range(0, len(matrix))]
    Gt = Graph.Graph(Vt, Et)
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if matrix[i][j] is 1:
                E[i].append(Graph.Arch(i, j))
                V[i].addAdj(V[j])
                Et[j].append(Graph.Arch(j, i))
                Vt[j].addAdj(Vt[i])
    DFS.DFS(G)
    sccList = [[] for i in range(0, len(Gt.V))]
    DFS.SCC(Gt, sccList)
    count = 0
    length = []
    for i in range(0,len(sccList)):
        if(len(sccList[i]) is not 0):
            count+=1
            length.append(len(sccList[i]))
            #print "SCC["+str(i)+"] : " + str(sccList[i])
    print "Ci sono in totale "+str(count)+" componenti fortemente connesse"
    print "Con il seguente numero di vertici al loro interno: ", length
