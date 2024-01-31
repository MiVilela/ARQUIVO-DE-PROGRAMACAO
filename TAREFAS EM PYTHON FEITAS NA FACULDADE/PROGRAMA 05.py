#Calcule a area e o perimetro de um quadrado
#(formulas : area = lado*lado e perimetro = 4*lado).
#       Tela:   Entre com o valor do lado: 6
#               A area vale: 36
#           O perimetro vale: 24


#Etapas:
#   1. Analisar e entender o problema
#   2. Definir os dados de entrada
#   3. Definir os processos(formulas) para encontrar dados de saida
#   4. Exibir os dados de saida
#   5. Testar o código com valores reais.

#   lado => 5   area => 25      perimetro =>  20

#   Definir os dados de entrada
lado = float (input ("Digite o valor do lado de um quadrad: "))

# Definir os processos(formulas)
area = lado*lado
perimetro = 4*lado


#Exibir os dados de saida
print ("A area vale : %.2f " %area)
print ("O perimetro vale : %.2f " %perimetro)




