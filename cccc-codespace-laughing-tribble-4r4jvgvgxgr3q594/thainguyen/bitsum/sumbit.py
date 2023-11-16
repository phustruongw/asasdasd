import time

# Lưu thời điểm bắt đầu
start_time = time.time()
with open('./thainguyen/sumbit/sumbit.inp','r') as fin:
    n=int(fin.readline())
def dembit(n):
    count=0
    for i in range(1,n+1):
        b=bin(i)[2:]    
        for bit in b:
            if bit =='1':
                count+=1
    return count
# result=0
# for i in range(1,n+1):
#     result+=dembit(i)
# print(result)
with open('./thainguyen/sumbit/sumbit.out','w') as fout:
    fout.write(str(dembit(n)))
for i in range(1000000):
    pass

# Lưu thời điểm kết thúc
end_time = time.time()

# Tính thời gian chạy
elapsed_time = end_time - start_time

print(f"Thời gian chạy: {elapsed_time} giây")