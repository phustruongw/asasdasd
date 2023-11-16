with open('./ct2016/CPDB/CPDB.INP','r') as fin:
    a,b=map(int,fin.readline().split())
def uoc(num):
    uoc=[]
    for i in range(1,int(num**0.5)+1):
        if num%i==0:
            uoc.append(i)
            if i!=num//i:
                uoc.append(num//i)
    return uoc
results=0
for j in range(a,b+1):
    if j%3==0 and len(uoc(j))==9:
        results += 1
with open('./ct2016/CPDB/CPDB.OUT','w') as fout:
    fout.write(str(results))