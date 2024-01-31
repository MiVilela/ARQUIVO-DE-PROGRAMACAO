cod = int(input('Qual o cargo? \n[1] - BALCONISTA \n[2] - VENDEDOR \n[3] - GERENTE \n:'))
h = float(input('Escreva a horas trabalhadas na semana:'))

if c==1:
    ST = 1500
    VH = (ST * 0.02)
    SB = h * VH
    print('Cargo:BALCONISTA')

elif c == 2:
    ST = 1800
    VH = (ST * 0.02)
    SB = h * VH
    print('Cargo:VENDEDOR')
elif c == 3:
    ST = 2300
    VH = (ST * 0.02)
    SB = h * VH
    print('Cargo:GERENTE')

print ('Salario Bruto : {:.2f}'.format(SB))

if SB <= 1000:
    IMP = SB * 0.09

elif SB >=1000.01 and SB <= 5000:
    IMP = SB * 0.10

else:
    IMP = SB * 0.12

print('Imposto Pago : {:.2f}'.format(IMP))

SR = SB - IMP
print('Salário a Receber:{:.2f}'.format(SR))




