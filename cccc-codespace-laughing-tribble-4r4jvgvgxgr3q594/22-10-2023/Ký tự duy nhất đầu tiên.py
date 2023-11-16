with open('./22-10-2023/stdin','r') as fin:
    a=int(fin.readline())
    result=[]
    import collections
    for i in range(a):
        str=fin.readline().strip()
        kq= collections.Counter(str)
        pt,sl=(zip(*kq.items()))
        for j in range(len(sl)):
            if sl[j]==1:
                result.append(j+1)
                break
            elif sl.count(1)==0:
                result.append(-1)
                break
with open('./22-10-2023/stdout','w') as fout:
    for u in range(len(result)):
        fout.write(f'{result[u]}\n')

a = int(input())  # Nhập số truy vấn

result = []
import collections

for i in range(a):
    s = input().strip()  # Nhập chuỗi ký tự
    kq = collections.Counter(s)
    pt, sl = zip(*kq.items())
    
    for j in range(len(sl)):
        if sl[j] == 1:
            result.append(j+1)
            break
        elif sl.count(1) == 0:
            result.append(-1)
            break

# In kết quả
for u in range(len(result)):
    print(result[u])