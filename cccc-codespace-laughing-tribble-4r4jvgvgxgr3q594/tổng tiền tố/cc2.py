with open('./tổng tiền tố/cc2.inp','r') as fin:
    n, m = map(int, fin.readline().split())

    MaxN = 6
    a = [[0] * MaxN for _ in range(MaxN)]
    s = [[0] * MaxN for _ in range(MaxN)]

    for i in range(1, n + 1):
        a[i][1:m+1] = map(int, fin.readline().split())
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + a[i][j]

    t = int(fin.readline())
    while t > 0:
        i, j, k, h = map(int, fin.readline().split())
        print(s[k][h] - s[i - 1][h] - s[k][j - 1] + s[i - 1][j - 1])
        t -= 1
