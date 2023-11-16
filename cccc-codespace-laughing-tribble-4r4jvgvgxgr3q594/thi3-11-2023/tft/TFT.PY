with open('TFT.INP','r') as fin:
    c=int(fin.readline())

def find_min_x_y(a, b, c):
    min_x = float("inf") 
    min_y = float("inf")

    for x in range(c // a + 1):
        for y in range(c // b + 1):
            if a * x + b * y == c:
                if x < min_x and y < min_y:
                    min_x = x
                    min_y = y

    return min_x, min_y

a = 2
b = 3


min_x, min_y = find_min_x_y(a, b, c)


if min_x != float("inf") and min_y != float("inf"):
    with open('TFT.OUT','w') as fout:
        fout.write(str(min_x)+' '+str(min_y))
else:
    with open('TFT.OUT','w') as fout:
        fout.write('-1')