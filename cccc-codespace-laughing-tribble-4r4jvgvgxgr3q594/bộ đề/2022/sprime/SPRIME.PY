with open('sprime.inp','r') as fin:
    t=int(fin.readline())
    l=[]
    r=[]
    for i in range(t):
        l1,r1=map(int,fin.readline().split())
        l.append(l1)
        r.append(r1)
def snt(num):
    nghiem=[]
    for q in range(1,int(num**0.5)+1):
        if num%q==0:
            nghiem.append(q)
            if q != num//q:
                nghiem.append(num//q)
    if len(nghiem) == 2:
        return num
def tcs(num1):
    tong=0
    while num1 >0:
        tong+=num1%10
        num1 = num1 //10
    return tong
soluong=[]
cacsodb=[]
for j in range(t):
    for o in range(l[j],r[j]):
        if snt(o)==o and tcs(o)%5==0:
            cacsodb.append(o)
    soluong.append(len(cacsodb))
    cacsodb.clear()
with open('sprime.out','w') as fout:
    for e in range(len(soluong)):
        fout.write(f'{soluong[e]}\n')