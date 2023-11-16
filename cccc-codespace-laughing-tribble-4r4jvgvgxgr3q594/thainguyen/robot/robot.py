with open('./thainguyen/robot/robot.inp','r') as fin:
    n=int(fin.readline())
    a=[]
    b=[]
    for i in range(n):
        a1,b1=fin.readline().split()
        a.append(a1)
        b.append(b1)
print(n)
print(a)
print(b)

# tạo 1 mảng f[] dài vô hạn
# mỗi bước đi lưu tọa độ vào 1 f[i] biến đếm +1 so sánh với các mảng trước
# nếu trùng in biến đếm ko trùng 