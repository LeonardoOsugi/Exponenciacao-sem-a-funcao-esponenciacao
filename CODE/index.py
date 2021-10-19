def exponenciacao(x,y,countx):
    for i in range(1, y):
        countx *= x
    expo = countx
    if y<0:
        for i in range(1,-y):
            countx *= x
        expo = 1/countx
    if y == 0:
        countx = 1
        expo = countx
    print('A base {} elevada ao expoente {} é igual a {}'.format(x,y,expo))
x = int(input('Digite um número qualquer: '))
y = int(input('Digite mais um número qualquer: '))
countx = x
exponenciacao(x,y,countx)