with open('./thi14-11-2023/tong/TONG.INP','r') as fin:
    t,x=map(int,fin.readline().split())
    for i in range(t):
        a,b=map(int,fin.readline().split())
        c=a+b
        with open('./thi14-11-2023/tong/TONG.OUT','a') as fout:
            fout.write(str(c)[:x]+'\n')