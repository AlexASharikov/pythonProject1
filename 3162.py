spis = list(map(int, input().split()))
counter = 1

for i in range(1, len(spis)):
    if spis[i] != spis[i - 1]:
        counter += 1
print(counter)