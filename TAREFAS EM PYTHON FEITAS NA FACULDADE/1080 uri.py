n = int(input())
x = 0

for c in range(1, 100):
    a = int(input())
    if a > x:
        maior = a
        posição = c + 1
        x = a
print(maior)
print(posição)