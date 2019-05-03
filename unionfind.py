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
# maximo vai ser a altura da arvore log(n)
    def Find(self, p):
        p = self.lista[p]
        if(p.id == int(p.cost)):
            return p
        else:
            print p.id
            return self.Find(p.id)

# 2*log(n)
    def Union(self, p, q):
        #p = self.lista[p]
        #q = self.lista[q]
        p = self.Find(p)
        q = self.Find(q)
        if (p.rank > q.rank):
            p, q = q, p
        p.id = int(q)
        q.rank += p.rank
        print q.rank



if False:
    g = Init(7)
    for x in g:
        print "ids:"+ str(int(Find(x))) + " rank:" + str(int(x.rank))
    print "compartimento do 1o e 3o sao o mesmo?" + str(Find(g[0]).id == Find(g[2]).id)
    print "joining primeiro e terceiro"
    Union(g[0], g[2])
    print "compartimento do 1o e 3o sao o mesmo?" + str(Find(g[0]).id == Find(g[2]).id)
    print "compartimento do 1o e 6o sao o mesmo?" + str(Find(g[0]).id == Find(g[5]).id)
    Union(g[0], g[5])
    print "compartimento do 1o e 6o sao o mesmo?" + str(Find(g[0]).id == Find(g[5]).id)

#sets =  [str(Find(x)) for x in g]

# loads a stored file where each line has one edge(u, v, cost)
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
    g = UF(7)
    mst = []
    edges.sort(key=lambda x: x.cost)
    for i in range(len(edges)):
        print g.lista
        print g.Find(edges[i].u), g.Find(edges[i].v)
        if g.Find(edges[i].u).id == g.Find(edges[i].v).id:
            continue
        else:
            print g.Find(edges[i].u).id, g.Find(edges[i].v).id
            g.Union(edges[i].u, edges[i].v)
            print g.Find(edges[i].u).id, g.Find(edges[i].v).id
            print edges[i].cost
            mst.append(edges[i].cost)
    print mst



a = load_graph_edges('graph.txt')
print a
"""print a
print "compartimento do 1o e 3o sao o mesmo?" + str(Find(a[a[0].u]).id == Find(a[a[2].v]).id)
print "joining primeiro e terceiro"
Union(a[0], a[2])
print "compartimento do 1o e 3o sao o mesmo?" +  str(Find(a[a[0].u]).id == Find(a[a[2].v]).id)
print a
"""
Kruskal(a)


