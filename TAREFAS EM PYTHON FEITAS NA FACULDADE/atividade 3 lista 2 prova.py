veiculo = float(input('Valor do veiculo na fabrica:'))

if veiculo<=1000:
    IPI = veiculo*0.10
elif veiculo>=1001.01 and veiculo<=5000:
    IPI = veiculo*0.30
else:
    IPI = veiculo*0.40

print('IPI: {}'.format(IPI))

if veiculo<=2000:
    ICMS = veiculo*0.03
elif veiculo>=2000.01 and veiculo<=3000:
    ICMS = veiculo*0.15
else:
    ICMS = veiculo*0.20

print('ICMS: {}'.format(ICMS))

final = veiculo+IPI+ICMS
print('VALOR FINAL: {}'.format(final))
