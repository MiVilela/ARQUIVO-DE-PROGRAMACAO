dias = int(input('Numero de dias trabalhados:'))
porcentagem = float(input('Porcentagem do imposto:'))
salario = dias * 50
imposto = (porcentagem*salario) / 100
QL = salario - imposto                                                     
print('Quantia Liquida: {:.2f}'.format(QL))
print('Dias Trabalhados: {}'.format(dias))
print('Imposto(%):{}'.format(porcentagem))

if QL<=1300:
    print('Não há tributação no Imposto de Renda')
else:
    print('Tributação no Imposto de Renda')