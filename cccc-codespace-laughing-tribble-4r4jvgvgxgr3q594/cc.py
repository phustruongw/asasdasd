def find_sequence(m, n):
    # Bước 1: Tìm tất cả ước số của n
    factors = []
    for i in range(1, m + 1):
        if n % i == 0:
            factors.append(i)

    # Bước 2: Sắp xếp danh sách ước số từ lớn đến bé
    factors.sort(reverse=True)

    # Bước 3: Khởi tạo xâu ban đầu
    result = ""

    # Bước 4: Lắp ghép xâu ban đầu từ các mẩu giấy
    for factor in factors:
        part_length = n // factor
        for i in range(1, factor + 1):
            part = "m" + str(i) + " "
            result += part * part_length

    return result

m = 6
n = 12
sequence = find_sequence(m, n)
print(sequence)
 