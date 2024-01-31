# dados 3 números diferentes, coloque-os em ordem crescente.



n1 = float (input ("Digite um número:"))
n2 = float (input ("Digite um número diferente:"))
n3 = float (input ("Digite outro número:"))



if (n1>n2) and (n2>n3): #teste 1
    print (n3," ", n2, " ", n1)

elif (n1>n3) and (n3>n2): #teste 2
    print (n2," ", n3, " ", n1)

elif(n2>n1) and (n1>n3): #teste 3
    print (n3," ", n1, " ", n2)

elif(n2>n3) and (n3>n1): #teste 4
    print (n1," ", n3, " ", n2)

elif(n3>n1) and (n1>n2): #teste 5
    print (n2," ", n1, " ", n3)

elif (n3> n2) and (n2>3): #teste 6
    print (n1," ", n2, " ", n3)
