cf = int(input("Código Funcional:"))
sal = float(input("Salário:"))
temp = float(input("Tempo:"))

if (sal <= 500.00):
    r = sal * (20.0/100.0)
    r = sal + r
elif(sal <= 1000.00):
    r = sal * (10.0/100.0)
    r = sal + r
elif(sal <= 1500.00):
    r = sal * (5.0/100.0)
    r = sal + r
else :
    r = sal
    print("Funcionario Sem Reajuste")


if(temp < 1):
    b = r
    print("Funcionário Sem Bônus")
elif(temp <= 3):
    b = r + 100.00
elif(temp <= 6):
    b = r + 200.00
elif(temp <= 9):
    b = r + 300.00
else:
    b = r + 500.00

print("Novo Salário: %.2f" %b)

cd = cf // 10 % 10
if(cd == 3):
 print("Parcela Unica:4000.00")
elif(cd == 2):
    print("Parcela Unica: 3000.00")
elif (cd == 1):
    print("Parcela Unica:1500.00")
else:
    print("Codigo nao encontrado")