import sys
t = int(input().strip())
for _ in range(t):
    n, x, y, d = map(int, input().split())
    ans = float('inf')
    if abs(x - y) % d == 0:
        ans = abs(x - y) // d
    else:
        # Roll to the start
        if (y - 1) % d == 0:
            ans = min(ans, (x - 1 + d - 1) // d + (y - 1) // d)
        # Roll to the end
        if (n - y) % d == 0:
            ans = min(ans, (n - x + d - 1) // d + (n - y) // d)

    if ans == float('inf'):
        print("-1")
    else:
        print(ans)
