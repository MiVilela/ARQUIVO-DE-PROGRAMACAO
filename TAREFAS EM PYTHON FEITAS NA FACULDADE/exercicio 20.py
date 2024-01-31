A = float(input('Digite um valor:'))
B = float (input('Digite outro valor:'))
C = float (input('Digite outro valor:'))

if (C < B + A) and (B < C + A) and (A < B+C):
    if (A!= B and B!= C and C!= A):
        print('Triângulo Escaleno! {A, B, C}')
    elif (A==B) or (A==C) or (B==C):
        print ('Triangulo Tsóceles! {A, B, C}')
    elif A==B and B==C and C==A:
        print('triangulo equilátero! {A, B, C}')
else:
    print("Não é um triangulo!")
            
    
