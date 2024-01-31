numero = int (input ("digite um numero : "))
centena = numero // 100
numero = numero % 100
dezena = numero // 10
unidade = numero % 10

soma = centena + dezena*10 + unidade*100

print (" numero invertido : %d" % soma)
