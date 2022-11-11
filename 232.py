a = int(input())
b = list(map(int, input().split()))

for i in range(1, a):
    var = b[i]
    j = i - 1
    while (j >= 0 and var < b[j]):
        b[j + 1] = b[j]
        j = j - 1
    b[j + 1] = var
print(*b)