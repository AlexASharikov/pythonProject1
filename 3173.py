s = list(map(int, input().split()))
x = s[0]
x_count = s.count(x)
for i in s:
    if s.count(i) > x_count:
        x = i
        x_count = s.count(i)
print(x)