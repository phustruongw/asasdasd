with open('SEQ.INP','r') as fin:
    n,k=map(int,fin.readline().split())
    lista=[]
    listd=[]
    for i in range(n):
        a1,b1=map(int,fin.readline().split())
        lista.append(a1)
        listd.append(b1)
        u=list(zip(lista,listd))
result=0
for j in range(n):
    a,d=u[j]
    if k>a and (k-a)%d==0:
        result+=1
with open('SEQ.OUT','w') as fout:
    fout.write(str(result))