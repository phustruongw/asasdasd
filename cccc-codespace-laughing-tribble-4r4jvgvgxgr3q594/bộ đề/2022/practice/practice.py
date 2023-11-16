with open('practice.inp','r') as fin:
    n,c=map(int,fin.readline().split())
    a=[]
    b=[]
    for k in range(n):
        a1,b1=map(int,fin.readline().split())
        a.append(a1)
        b.append(b1)
gop=list(zip(a,b))
gop.sort(key=lambda x: x[0])
a,b=zip(*gop)
results=0
for i in range(n):
    if c>=a[i]:
        c+=b[i]
        results+=1
with open('practice.out','w') as fout:
    fout.write(str(results))