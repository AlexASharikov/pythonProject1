a = int(input())
b = list(map(int, input().split()))
counter = 0

for i in range(a - 1, 0, -1):
    for j in range(0, i):
        if b[j + 1] < b[j]:
            b[j], b[j + 1] = b[j + 1], b[j]
            counter += 1
print(counter)