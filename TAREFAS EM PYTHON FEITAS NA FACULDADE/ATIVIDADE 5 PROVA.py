comp = int(input('Qual tipo de computador? \n[1] - Desktop 1900.00 \n[2] = Notebook 3600.00 \nOpção:'))
taxa = int(input('Qual estado? \n[1] - MG 10% \n[2] - SP 12% \n[3] - RJ 15% \nOpção:'))

if comp==1 and taxa==1:
    imp = 1900 + (1900*0.10)
    print('Valor da entrega: {:.2f}'.format(imp))
elif comp==1 and taxa==2:
    imp = 1900 + (1900*0.12)
    print('Valor da entrega: {:.2f}'.format(imp))
elif comp==1 and taxa==3:
    imp = 1900 + (1900*0.15)
    print('Valor da entrega: {:.2f}'.format(imp))
elif comp==2 and taxa==1:
    imp = 3600 + (3600*0.10)
    print('Valor da entrega: {:.2f}'.format(imp))
elif comp==2 and taxa==2:
    imp = 3600 + (3600*0.12)
    print('Valor da entrega: {:.2f}'.format(imp))
elif comp==2 and taxa==3:
    imp = 3600 + (3600*0.15)
    print('Valor da entrega: {:.2f}'.format(imp))
elif (comp< 1 or comp >2) and (taxa >= 1 or taxa <= 3):
    print('Opção de Equipamento invalido')
elif (taxa < 1 or taxa >3) and (comp >= 1 or comp <= 2):
    print('Opção de Estado invalido')
else:
    print('Opção de Estado invalido')
    print('Opção de Equipamento invalido')