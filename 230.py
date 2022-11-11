a = int(input())
b = list(map(int, input().split()))
for i in range(0, a - 1):
    _min = i
    for j in range(i + 1, a):
        if b[j] < b[_min]:
            _min = j
    b[i], b[_min] = b[_min], b[i]
print(*b)