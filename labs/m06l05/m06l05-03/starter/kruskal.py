edges = [(1,'A','B'),(2,'B','C'),(3,'A','C'),(4,'B','D'),(5,'C','D')]
nodes = ['A','B','C','D']
idx = {n:i for i,n in enumerate(nodes)}
parent = list(range(4))
rank = [0]*4
def find(x):
    if parent[x]!=x: parent[x]=find(parent[x])
    return parent[x]
def union(x,y):
    a,b=find(x),find(y)
    if a==b: return False
    if rank[a]<rank[b]: a,b=b,a
    parent[b]=a
    if rank[a]==rank[b]: rank[a]+=1
    return True
total=0
for w,u,v in sorted(edges):
    if union(idx[u],idx[v]):
        print(u,'-',v,'weight',w)
        total+=w
print('total:',total)
