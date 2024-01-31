valor = float(input(''))
if valor <= 2000.00:
    i = 0
    print('Isento')
if 2000.00 < valor <= 3000.00:
    valor8 = valor - 2000.00
    i = valor8 * (8 / 100)
if 3000.00 < valor <= 4500.00:
    i8 = (8/100) * (1000.00)
    valor18 = valor - 3000.00
    i = valor18 * (18/100) + i8

if valor > 4500.00:
    i8 = (8/100) * (1000.00)
    i18 = (18 / 100) * (1500.00)
    valor28 = valor - 4500.00
    i = i18 + i8 + valor28 * (28 / 100)

if valor > 2000.00:
    i = float(i)
    print('R${:.2f}'.format(i))