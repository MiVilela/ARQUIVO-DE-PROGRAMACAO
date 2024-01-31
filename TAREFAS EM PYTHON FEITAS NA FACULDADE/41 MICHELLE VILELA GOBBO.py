# EXERCICIO41

# IMC = (altura*altura) / peso

p = float(input('Digite o peso:'))
h = float(input('Digite a altura:'))

imc = p / (h * h)

if (imc<18.5):
    print('Abaixo do peso')
elif(imc<=24.9):
    print('Saudavel')
elif(imc<=29.9):
    print('Peso em excesso')
elif(imc<=34.9):
    print('Obesidade Grau I')
elif(imc<=39.9):
    print('Obesidade Grau II(severa)')
else:
    print('Obesidade Grau III(morbida)')