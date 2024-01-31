#ler 5 valores e calcular a media
lista=[]
soma = 0
for i in range (5):
    n = int(input('Digite um numero: '))
    lista.append(n)
    soma = soma + lista[i]
print(soma/5.0)