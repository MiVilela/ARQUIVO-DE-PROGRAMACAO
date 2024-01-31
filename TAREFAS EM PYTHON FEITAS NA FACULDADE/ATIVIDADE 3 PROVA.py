TrabLab = float(input('Digite a nota do trabalho:'))
AvM = float(input('Digite a nota da prova mensal:'))
ExF = float(input('Digite a nota do exame final:'))
media = (TrabLab*3 + AvM*4 + ExF*3) / 10
print('Media:{:.2f}'.format(media))
if media>=0 and media<=2.9:
    print('Aluno Reprovado')
elif media>=3 and media<=4.9:
    print('Aluno de recuperação')
elif media>=5 and media<=10:
    print('Aluno Aprovado')
else:
    print('Erro:Entrada de dados')