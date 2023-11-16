with open('./tổng tiền tố/cc.inp','r') as fin:
    n=int(fin.readline())
    a=list(map(int,fin.readline().split()))
    t=int(fin.readline())
    tonga=[0,a[0]]
    for i in range(1,n):
        tonga.append(a[i]+tonga[i])
    for j in range(t):
        l,r=map(int,fin.readline().split())
        print(tonga)
        print(l,r)
        print(tonga[r],tonga[l-1])
        print(tonga[r]-tonga[l-1])