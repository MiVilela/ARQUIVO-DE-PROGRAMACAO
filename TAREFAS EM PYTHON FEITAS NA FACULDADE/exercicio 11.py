n = int(input('digite um número:'))

if(n >=0):
    centena = n // 100

    n = n%100
    dezena = n // 10
    unidade = n%10

    print (centena, " ", dezena, " ", unidade)
    print ('Soma:', centena+dezena+unidade)

else:
    print ('numero invalido')
