n,k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
count = 0

for j in range(0,k):
    for i in range(0,n):
        if b[j] == a[i]:
            print("YES")
            break
        if i == n - 1:
            print("NO")
