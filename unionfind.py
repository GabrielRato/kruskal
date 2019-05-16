import sys

class Node:
    def __init__(self, id, cost=0, u=-1, v=-1):
        self.id = id
        self.cost = cost
        self.u = u
        self.v = v
        self.rank = 1

    def __str__(self):
        return str(self.id)

    def __int__(self):
        return self.id
    __repr__ = __str__

# init a class of nodes with size n
def Init(n):
    myset = []
    for x in range(n):
        myset.append(Node(x, x))
    return myset

class UF:
    def __init__(self, n):
        self.lista = Init(n)

# caso o representante de classe, id, nao seja ele mesmo seu propio pai, que no caso
# to emulando com o cost,
# maximo vai ser a altura da arvore log(n)
    def Find(self, p):
        p = self.lista[p]
        if(p.id == int(p.cost)):
            return p
        else:
            return self.Find(p.id)

    def Union(self, p, q):
# hora de encontrar nosso representante de classe
        p = self.Find(p)
        q = self.Find(q)
        if (p.rank > q.rank):
            p, q = q, p
        p.id = int(q)
        q.rank += p.rank

# loads a stored file where each line has one edge(u, v, cost)
# and stores it into Nodes
def load_graph_edges(filename):
    a = []
    idx = 0
    with open(filename, 'r') as _file:
        for line in _file:
            u, v, cost = line.split()
            a.append(Node(int(u), int(cost), int(u), int(v)))
            idx += 1
    return a

def Kruskal(edges):
    pesos = 0
    # init my Union Find struct
    g = UF(7)
    # now sort edges by cost
    edges.sort(key=lambda x: x.cost)
    with open('mst.txt', 'w') as _file:
        # iterate over all edges, we must choose wich one to keep into final
        # mst
        for i in range(len(edges)):
            u = edges[i].u
            v = edges[i].v
            # somewhere we have to ugly the code
            if g.Find(u).id == g.Find(v).id:
                continue
            else:
                g.Union(u, v)
                _file.write(str(u) + ' ' + str(v) +
                ' ' + str(edges[i].cost) + '\n')
                pesos += edges[i].cost
    print 'final size of UF: '+ str(sys.getsizeof(g))
    print 'final size of Graph: '+ str(sys.getsizeof(edges))
    print pesos


a = load_graph_edges('graph2.txt')
Kruskal(a)
