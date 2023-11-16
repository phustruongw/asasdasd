with open('TONGUOC.INP','r') as fin:
    a,b=map(int,fin.readline().split())
def uoc(n):
    uoc=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            uoc.append(i)
            if n//i != i:
                uoc.append(n//i)
    return uoc
result=0
uoca=uoc(a)
uocb=uoc(b)
for j in range(len(uoca)):
    x=uoca[j]
    for t in range(len(uocb)):
        if 3*x==uocb[t]:
            result+=x
if result!=0:
    with open('TONGUOC.OUT','w') as fout:
        fout.write(str(result))
else:
    with open('TONGUOC.OUT','w') as fout:
        fout.write('0')