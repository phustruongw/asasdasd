with open('./ct2020/TONGCAPSO.INP','r') as fin:
    n=int(fin.readline().strip())
    a=[]
    b=[]
    for i in range(n):
        a1,b1=map(int,fin.readline().strip().split())
        a.append(a1)
        b.append(b1)
result=[]
for j in range(len(a)):
    if (a[j]+b[j])%2==0:
        result.append(a[j]+b[j])
with open('./ct2020/TONGCAPSO.OUT','w') as fout:
    for u in range(len(result)):
        fout.write(f'{result[u]}\n')