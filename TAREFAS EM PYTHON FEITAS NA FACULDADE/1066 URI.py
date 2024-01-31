w = 0
x = 0
y = 0
z = 0
for c in range(5):
    num = int(input())
    if num % 2 == 0:        #numero par
        x += 1
    if num % 2 == 1:        #numero impar
        y += 1
    if num > 0:             #positivo
        w += 1
    if num < 0:             #negativo
        z += 1
print('{} valor(es) par(es)'.format(x))
print('{} valor(es) impar(es)'.format(y))
print('{} valor(es) positivo(s)'.format(w))
print('{} valor(es) negativo(s)'.format(z))
