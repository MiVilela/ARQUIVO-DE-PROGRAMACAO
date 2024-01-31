custofabrica = float(input('Digite o custo de fabrica:'))

if(custofabrica<=12000):
    c = custofabrica + (custofabrica*0.05)

elif(custofabrica<=25000):
    c = custofabrica + (custofabrica*0.10)

elif(custofabrica>25000):
    c = custofabrica + (custofabrica*0.15)

if (custofabrica<=12000):
    i = 0
elif(custofabrica<=25000):
    i = custofabrica*0.15
    
elif(custofabrica>25000):
    i = custofabrica*0.20

CustoFinal = c + i

print('Custo Final é de:%.2f' %CustoFinal)
