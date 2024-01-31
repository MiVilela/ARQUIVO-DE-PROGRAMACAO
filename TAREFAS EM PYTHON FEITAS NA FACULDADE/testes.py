n = int(input())
h = 0
i = 1
while (i<=n):
    h = h + 1/i
    i = i+1
print('{:.6f}'.format(h))