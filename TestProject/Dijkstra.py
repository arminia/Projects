from collections import namedtuple

import  heapq
import queue

class Vertex:

    label = ''
    adj = []
    dist = []
    cost = 0
    predec = ''

    def __init__(self, l ,a , d, c, p):

        self.label= l
        self.adj= a
        self.dist = d
        self.cost = c
        self.predec = p



def cnstr_graph(file):

    G=[]
    adj1=[]
    dist1=[]
    s=0

    for line in file:


        nums = line.split()

        l = 0
        for i in range(len(nums)-1):
            couple=nums[i+1]


            l += 1

            adj1.append(couple[1])
            dist1.append(couple[3])


        Vertices = Vertex(nums[0], adj1[s:s+l], dist1[s:s+l], 1000000, 'null')

        G.append(Vertices)

        s = s+l


    return G

def Graph(file):

    VertexInfo= namedtuple("VertexInfo", "vert, adj, dist, cost, prev")
    #VertexInfo2 = namedtuple("VertexInfo2", "adj, dist")

    G=[]
    G2=[]
    adj1=[]
    dist1=[]
    s = 0

    for line in file:


        nums = line.split()

        l = 0
        for i in range(len(nums)-1):
            couple=nums[i+1]


            l += 1

            adj1.append(couple[1])
            dist1.append(couple[3])


        info = VertexInfo(vert = nums[0], adj = adj1[s:s+l], dist = dist1[s:s+l], cost= '1000000', prev= 'null')

        G.append(info)

        s = s+l




    return G


def Dijkstra(G, source):

    #Q = queue.Queue(len(G))
    heap = []

    for i in range(len(G)):
        G[i].cost = 1000000
        G[i].predec = 'null'

    G[vrtndx(G, source)].cost = 0

    for i in range(len(G)):
        heapq.heappush(heap, (G[i].cost, G[i].label))

    while len(heap) > 0:

        u_mincost= heapq.heappop(heap) #it's a tuple!

        #u= G[vrtndx(G, u_mincost[1])].label
        u = G[vrtndx(G, u_mincost[1])]


        for v in u.adj:

            uindex= vrtndx(G,u.label)
            #uneighbors = G[uindex].adj
            vindex= adjnx(G[uindex].adj,v)

            alt = G[uindex].cost + int(G[uindex].dist[vindex])

            if alt < G[vrtndx(G,v)].cost:
                G[vrtndx(G, v)].cost= alt
                G[vrtndx(G, v)].prev= u


    return report(G)









def report(G):

    rep = []
    for i in range (len(G)):

        rep.append((G[i].label, G[i].cost))

    return rep


def vrtndx(G, char):

    for i in range(len(G)):
        if G[i].label == char:
            return i


def adjnx(A, char):

    for i in range(len(A)):
        if A[i]== char:
            return i

def Main():

    f = open('dijgraph.txt','r')

    graph = {
        'B': {'A': 5, 'D': 1, 'G': 2},
        'A': {'B': 5, 'D': 3, 'E': 12, 'F': 5},
        'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
        'G': {'B': 2, 'D': 1, 'C': 2},
        'C': {'G': 2, 'E': 1, 'F': 16},
        'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
        'F': {'A': 5, 'E': 2, 'C': 16}}




    G = cnstr_graph(f)

    #for i in range (len(G)):
     #   verclass.append(Vertex(G[i].vert,  G[i].adj, G[i].dist, G[i].cost))


    #G[2].cost[0] = '344'


    f.close()

    print(Dijkstra(G, 'd'))





if __name__=='__main__':
    Main()