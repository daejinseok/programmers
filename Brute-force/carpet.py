import math

def y(n):
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0 :
            yield (int(n/i), i)


for i in range(24):
    a = y(i)
    for j in a:
        print(i, j)