n = int(input())

for i in range(1, n + 1):
    a = float(input())
    b = float(input())
    c = float(input())
    resultado = (a * 2 + b * 3 + c * 5) / 10
    print('{:.1f}'.format(resultado))