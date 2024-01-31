x = 0
m = 0
for c in range(1, 7):
    num = int(input())
    if num > 0:
        x = x + 1
        m = m + num
print('{} valores positivos'.format(x))
print('{:.1f}'.format(m))