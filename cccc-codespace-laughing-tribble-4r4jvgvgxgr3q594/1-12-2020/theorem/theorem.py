with open('theorem.inp','r') as fin:
    a=int(fin.readline())
def ptsnt(N):
    b = []
    i = 2
    while i * i <= N:
        if N % i:
            i += 1
        else:
            N //= i
            b.append(i)
    if N > 1:
        b.append(N)
    return b
c=ptsnt(a**2)
import collections
d = collections.Counter(c)
ptu,sl=zip(*d.most_common())
q=1
for i in range(len(sl)):
    q=(sl[i]+1)*q
with open('theorem.out','w') as fout:
    fout.write(str(q))
