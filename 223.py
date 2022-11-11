n = int(input())
a = list(map(int, input().split()))
x = int(input())
counter = 0

for i in range(0,n):
    if a[i] == x:
        counter += 1
print(counter)