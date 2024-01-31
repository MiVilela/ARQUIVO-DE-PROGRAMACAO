i = 1
while (i <=7):
    temp = int(input('Digite a temperatura:'))
    if (i==1):
        maior = temp
        dia = 1
    elif (temp > maior):
        maior = temp
        dia = 1
    i = i+ 1

if (dia ==1):
    dia = 'domingo'
elif dia==2:
    dia = 'Segunda'
elif dia == 3:
    dia = 'terça'
elif dia==4:
    dia = 'quarta'
elif dia==5:
    dia = 'quinta'
elif dia==6:
    dia = 'sexta'
else:
    dia = 'Sabado'


print('A maior temperatura foi {} no dia {}'.format(maior, dia))