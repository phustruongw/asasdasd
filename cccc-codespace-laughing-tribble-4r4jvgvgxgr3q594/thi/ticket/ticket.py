with open('./thi/ticket/ticket.inp','r') as fin:
    n,m=map(int,fin.readline().split())
    h=list(fin.readline().split())
    t=list(fin.readline().split())
h.sort(reverse=True)
result=[]
for i in range(n):
    if t[i]<h[-1]:
        result.append(-1)
    for j in range(len(h)):
        if t[i]>=h[j]:
            result.append(h[j])
            del h[j]
            break
if n<m:
    for n in range(m-n):
        result.append(-1)
with open('./thi/ticket/ticket.out','w') as fout:
    for a in range(len(result)):
        fout.write(f'{result[a]}\n')