# cpf => "2 8 0 0 1 2 3 8 9"
# lista => 0 1 2 3 4 5 6 7 8
# dig10 = 0, 2, 18, ...
estado = ['RS', 'DF GO MS MT TO','AC AM AP PA RO RR','CE MA PI','AL PB PE RN','BA SE','MG', 'ES RJ', 'SP', 'PR SC']

cpf = input('Digite seu CPF: ')
dig10=0
tamanho = len(cpf)  #tamanho => 9
for x in range(tamanho):    #x [0,1,2,3...,8]0
    dig10 = dig10 + int(cpf[x]) * (x+1)
dig10 = dig10 % 11

cpf = cpf+str(dig10)
dig11 = 0
for x in range(10):
    dig11 = dig11 + int(cpf[x]) * x
dig11 = dig11 % 11
if(dig11==10):
    dig11=0
cpf = cpf + str(dig11)
print(cpf)

print(estado [int (cpf[8])])