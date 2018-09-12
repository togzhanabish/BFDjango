import math
a = int(input())
b = int(input())


for i in range(a, b + 1):
    p = int(math.sqrt(i))
    if p * p == i:
        print(str(i) + " ")