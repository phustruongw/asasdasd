t=int(input())
nganxep=[]
for i in range(t):
    line = input().strip().split()
    if int(line[0])==1:
        nganxep.append(int(line[1]))
    elif int(line[0])==2:
        if nganxep:
            nganxep.pop()
    elif int(line[0])==3:
        if len(nganxep)==0:
            
                print('Empty!'+'\n')
        else:
            
                print(str(nganxep[-1])+'\n')