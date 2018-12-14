from collections import namedtuple

import queue



class Vertex:

    def __init__(self, m, l, n):

        self.marked = m
        self.label = l
        self.neighbors = n

def graph(file):

    VertexInfo = namedtuple("VertexInfo", "vert, adj, flag")

    G=[]
    for line in file:

        nums = line.split()

        info = VertexInfo(vert=nums[0], adj=nums[1:], flag='0')

        G.append(info)

    return G

def BFS(G):

    Q = queue.Queue(maxsize= len(G)*(len(G)+1))

    report= []

    VertexInfo = namedtuple("VertexInfo", "vert, adj, flag")

    info = VertexInfo(vert=G[0].vert, adj= G[0].adj, flag= '1')

    G[0] = info

    v = G[0]

    Q.put(v)

    report.append(v.vert)


    while Q.empty() == False:
        v = Q.get()
        for adj in v.adj:
            adj = int(adj)
            if G[adj-1].flag == '0':
                info = VertexInfo(vert=G[adj-1].vert, adj=G[adj-1].adj, flag='1')
                G[adj-1]= info
                Q.put(G[adj-1])
                report.append(G[adj-1].vert)

    return report





def Main():

    G =[]

    file = open('bfsgraph.txt', 'r')

    G = graph(file)

    file.close()

    print(BFS(G))


if __name__ == "__main__":
    Main()