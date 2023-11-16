import time

# Lấy thời điểm bắt đầu
start_time = time.time()
with open('./thi/candy/candy.inp','r') as fin:
    n=fin.readline()
    a=list(fin.readline().split())
l=0
r=2
result=0
for i in range(int(n)):
    if len(set(a[l:r]))==2:
        result=max(result,len(a[l:r]))
        r+=1
    else:
     r+=1
     l+=1
with open('./thi/candy/candy.out','w') as fout:
    fout.write(str(result))
end_time = time.time()

# Tính thời gian thực thi
execution_time = end_time - start_time
print("Thời gian thực thi:", execution_time, "giây")


