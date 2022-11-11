n = int(input())
a = list(map(int, input().split()))
x = int(input())
c = []


for i in range(0,n):
    if a[i] == x:
        c.append(i+1)
print(*c)