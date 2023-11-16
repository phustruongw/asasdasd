with open('KSUM.INP','r') as fin:
    n,k=map(int,fin.readline().split())
    a=list(map(int,fin.read().split()))
tonga=[0,a[0]]
for i in range(1,n):
    tonga.append(a[i]+tonga[i])
maxsum=0
for j in range(k,n+1):
    maxsum=max(maxsum,tonga[j]-tonga[j-k])
with open('KSUM.OUT','w') as fout:
    fout.write(str(maxsum))