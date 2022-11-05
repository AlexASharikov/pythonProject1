spis = list(map(int, input().split()))

for i in range(len(spis), 0, -1):
    if i == len(spis):
        k = spis[i - 1]
    else:
        spis[i] = spis[i - 1]
spis[0] = k
print(*spis)