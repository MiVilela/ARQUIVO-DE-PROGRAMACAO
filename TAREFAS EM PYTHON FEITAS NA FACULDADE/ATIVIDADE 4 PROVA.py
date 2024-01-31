import math
a,b,c = input().split()
a= float (a)
b= float (b)
c= float (c)


if (a>b and b>c):
    print ("Crescente : %.2f %.2f %.2f" %(c,b,a))
    maior = a
    menor = c
elif (a>c and c>b):
    print ("Crescente : %.2f %.2f %.2f" %(b,c,a))
    maior = a
    menor = b
elif (b>a and a>c):
    print ("Crescente : %.2f %.2f %.2f" %(c,a,b))
    maior = b
    menor = c
elif (b>c and c>a):
    print ("Crescente : %.2f %.2f %.2f" %(a,c,b))
    maior = b
    menor = a
elif (c>a and a>b):
    print ("Crescente : %.2f %.2f %.2f" %(b, a, c))
    maior = c
    menor = b
elif (c>b and b>a):
    print ("Crescente : %.2f %.2f %.2f" %(a,b,c))
    maior = c
    menor = a
media = (a+b+c) /maior
expoente = 1.0/3.0
mediaG = (a*b*c) ** expoente
area = math.pi*menor**2
print('media: {:.4f}'.format(media))
print('media geometrica:{:.4f}'.format(mediaG))
print('Area : {:.5f}'.format(area))