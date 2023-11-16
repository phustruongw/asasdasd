import math
with open('./thainguyen/number/number.inp','r') as fin:
    n=int(fin.readline())
def uoc(n):
    uoc=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            uoc.append(i)
            if n//i!=i:
                uoc.append(n//i)
    return uoc
for i in range(n,10**9+1):
    if len(uoc(i))==4:
        with open('./thainguyen/number/number.out','w') as fout:
            fout.write(str(i))
        break