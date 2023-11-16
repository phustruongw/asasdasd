with open('./sieusonguyento/sieunt.inp','r') as fin:
    a=int(fin.readline())
def snt(n):
    max=10**n
    min=10**(n-1)
    snt=[True]*(max+1)
    snt[0]=snt[1]=False
    p=2
    while(p*p<=max):
        if(snt[p]):
            for i in range(p*p,max+1,p):
                snt[i]=False
        p+=1
    listsnt=[i for i in range(min,max+1) if snt[i]]
    return listsnt
results=[]
def check(num):
    num_str=str(num)
    for t in range(a):
        nnc=int(num_str[:t]+num_str[t+1:])
        if not snt(nnc):
            return False
    return True
x=snt(a)
# for q in range(len(x)):
#     if(check(x[q])):
#         results.append(x[q])
# print(results)
for c in range(len(x)):
    print(check(x[c]))