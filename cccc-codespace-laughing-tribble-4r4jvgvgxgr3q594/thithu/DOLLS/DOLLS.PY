with open('DOLLS.INP','r') as fin:
    n,k=map(int,fin.readline().split())
    a=list(map(int,fin.readline().split()))
a.sort(reverse=True)
result=a[0]
j=0
for i in range(1,len(a)):
    if a[i]+k<=a[j]:
        j+=1
    else:
        result+=a[i]
with open('DOLLS.OUT','w') as fout:
    fout.write(str(result))