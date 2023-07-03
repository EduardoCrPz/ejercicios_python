def mandel(c):
    cont = 0
    z = c
    while (abs(z)<2) and (cont<80):
        cont=cont+1
        z = z*z+c
        print(z)
    pass

a=0.2+0.6j
mandel(a)