class Node:
    def __init__(self, id):
        self.id = id
        self.rank = 1

    def __int__(self):
        return self.id

# init a class of nodes with size n
def Init(n):
    myset = []
    for x in range(n):
        myset.append(Node(x))
    return myset

# maximo vai ser a altura da arvore log(n)
def Find(p):
    if(p.id == int(p)):
        return p
    else:
        p.id = Find(p.id)
        return Find(p.id)

# 2*log(n)
def Union(p, q):
    p = Find(p)
    q = Find(q)
    if (p.rank > q.rank):
        p, q = q, p
    p.id = int(q)
    q.rank += p.rank


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



