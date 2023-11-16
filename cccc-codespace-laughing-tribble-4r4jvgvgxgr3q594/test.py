import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def count_prime_sums(n):
    count = 0
    for x in range(int(math.sqrt(n)) + 1):
        for y in range(int(n ** 0.25) + 1):
            num = x**2 + y**4
            if num <= n and is_prime(num):
                count += 1
    return count
n=int(input())
result=[]
f=[0]*n
for i in range(n):
    f[i]=int(input())
for j in range(n):
    result.append(count_prime_sums(f[j]))
for u in range(n):
    print(result[u])


# def is_square(n):
#     # Kiểm tra xem n có phải là số thực không âm và không có phần ảo.
#     if n.real >= 0 and n.imag == 0:
#         # Tính căn bậc hai của n và chuyển thành số nguyên.
#         root = int(n ** 0.5)
#         # Kiểm tra xem n có bằng bình phương của root.
#         return root * root == n
#     # Trả về False nếu n không thỏa mãn điều kiện ở trên.
#     return False
# print(is_square(12))