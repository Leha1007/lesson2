n = int(input())
p = ''
for i in range(1, n // 2 + 1):
    for j in range(1, n - i + 1):
        if n % (i + j) == 0 and i != j:
            p += str(i) + str(j)
print(p)
