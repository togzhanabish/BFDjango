a = int(input())

for i in range(2, a):
    if a % i == 0:
        a = min(a, i)
print(a)