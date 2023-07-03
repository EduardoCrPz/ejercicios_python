"""import random
import time

def valido(b):
    v = True
    for i in range(len(b)-1):
        if (b[i]>b[i+1]):
            v = False
    return v

def creaA(n):
    a = []
    while (len(a)<n):
        ale=random.randint(1,n)
        if not(ale in a):
            a.append(ale)
    return a
n = 3
a = creaA(n)
print(a)
parar = False
intentos = 0
inicio = time.time()
while not(parar):
    b = creaA(n)
    intentos = intentos + 1
    if valido(b):
        parar = True
print(b)
fin = time.time()
print("intentos: ", intentos)
print("tiempo: ", fin-inicio)"""
 

nac=set(["aleman","ingles","noruego"])
beb=set(["leche","agua","cerveza"]) 

for n1 in nac:
    for n2 in (nac-set([n1])):
        n3 = str (nac-set([n1,n2]))
        for b1 in beb:
            for b2 in (beb-set([b1])):
                b3= str (beb-set([b1,b2]))
                print(n3+b3)