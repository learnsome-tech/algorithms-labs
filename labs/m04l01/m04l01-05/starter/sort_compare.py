import random
def ins(a):
    a,c=a[:],0
    for i in range(1,len(a)):
        k,j=a[i],i-1
        while j>=0 and a[j]>k:a[j+1]=a[j];j-=1;c+=1
        a[j+1]=k
    return c
def mrg(a):
    if len(a)<=1:return a,0
    h=len(a)//2;L,cl=mrg(a[:h]);R,cr=mrg(a[h:])
    o=[];i=j=c=0
    while i<len(L) and j<len(R):
        c+=1;t=L[i]<=R[j];o.append(L[i]if t else R[j]);i+=t;j+=1-t
    return o+L[i:]+R[j:],cl+cr+c
def qks(a):
    if len(a)<=1:return a,0
    p=a[0];L=[x for x in a[1:]if x<=p];R=[x for x in a[1:]if x>p]
    l,cl=qks(L);r,cr=qks(R);return l+[p]+r,cl+cr+len(a)-1
for n in [10,50,100]:
    random.seed(1);d=[random.randint(0,99) for _ in range(n)]
    _,m=mrg(d);_,q=qks(d);print(f'n={n}: ins={ins(d)}, mrg={m}, qks={q}')
