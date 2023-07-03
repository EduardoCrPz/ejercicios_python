def ulam(n):
    cad=""    
    while (n>1):
        cad=cad+str(n)+"-"
        if ((n%2)==0):
            n=n//2
        else:
            n=n*3+1
    return cad[:-1]

def ulamNumPasos(n):
    cont=0    
    while (n>1):
        cont=cont+1
        if ((n%2)==0):
            n=n//2
        else:
            n=n*3+1
    return cont

for c in range(1,100):
    print(c,ulamNumPasos(c))

for c in range(1000):
    pasos=ulamNumPasos (c)
    if (pasos>100):
        print(c,100)
