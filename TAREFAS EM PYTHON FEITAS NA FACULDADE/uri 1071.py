x = int(input())
y = int(input())

if (x > y):
    auxiliar = x
    x = y
    y = auxiliar
soma =  0
contador = x
if (contador%2 == 1):
    contador = contador + 2
else:
    contador = contador + 1

while (contador < y):
    soma = soma + contador
    contador = contador + 2
print(soma)
