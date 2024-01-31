import math

logaritmo = float (input("Logaritmo: "))
base = float (input ("Qual a base : "))
if (logaritmo >=0):
    print (math.log(logaritmo,base))
else:
    print ('numero invalido')
