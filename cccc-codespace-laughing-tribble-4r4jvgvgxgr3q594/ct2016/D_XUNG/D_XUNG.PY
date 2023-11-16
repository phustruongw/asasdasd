with open('./ct2016/D_XUNG/D_XUNG.INP','r') as fin:
    xau = list(fin.readline().strip())
    k = int(fin.readline())
    L = []
    R = []
    for i in range(k):
        l,r = map(int,fin.readline().split())
        L.append(l)
        R.append(r)
xaucon=[]
for j in range(k):
    for o in range(L[j]-1,R[j]):
        xaucon.append(xau[o])
    if xaucon==xaucon[::-1]:
        with open('./ct2016/D_XUNG/D_XUNG.OUT','a') as fout:
            fout.write('yes'+'\n')
        xaucon.clear()
    else:
        with open('./ct2016/D_XUNG/D_XUNG.OUT','a') as fout:
            fout.write('no'+'\n')
        xaucon.clear()    

