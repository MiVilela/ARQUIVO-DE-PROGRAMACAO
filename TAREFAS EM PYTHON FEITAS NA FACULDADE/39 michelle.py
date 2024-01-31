salario = float(input('Digite o salário do funcionário:'))
tempo = int(input('Digite o tempo de serviço do funcionário na empresa:'))

if(salario<=500):
    s = salario * 1.25
    
elif(salario<=1000):
    s = salario * 1.20
 
elif(salario<=1500):
    s = salario * 1.15
    
elif(salario<=2000):
    s = salario * 1.10
   
else:
    s = salario
    
if(tempo<=1):
    bonus = 0
    
elif(tempo<=3):
    bonus = 100
    
elif(tempo<=6):
    bonus = 200

elif (tempo<=10):
    bonus = 300
    
else:
    bonus = 500


SalarioFinal = s + bonus

if (salario == SalarioFinal):
    print ('Não teve reajuste, nao teve bonus')
else:
    print('Salario Reajustado: %.2f' %SalarioFinal)
