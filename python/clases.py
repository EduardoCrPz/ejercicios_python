"""class Persona:
    nombre= ""
    edad= 0
    sueldo= 0.0
Persona1= Persona()
Persona2= Persona()

Persona1.nombre="pedro"
Persona1.edad=30
Persona1.sueldo=88.4

print (Persona1.nombre)"""

"""import time
from typing import Text
class cosa:
    nombre=""
    peso=10
    valor=0
    def __init__(self,n ,p ,v ): 
        self.nombre=n
        self.peso=p
        self.valor=v
casa= []
casa.append(cosa('Pintura',5,600))
casa.append(cosa('STEREO',7,1500))
casa.append(cosa('computadora',3,4000))
casa.append(cosa('Microondas',4,700))
casa.append(cosa('sombrilla',1,80))
casa.append(cosa('Calculadora',1,400))
casa.append(cosa('Botas',1,300))
casa.append(cosa('Balon',1,120))
casa.append(cosa('JARRON',1,30))
casa.append(cosa('Cuadro',2,600))
casa.append(cosa('Maleta',2,800))
casa.append(cosa('Radio',3,450))
casa.append(cosa('Silla',1,300))
casa.append(cosa('TELEFONO',1,800))
casa.append(cosa('Xbox',2,6000))
casa.append(cosa('florero',1,250))
casa.append(cosa('Luces',2,800))
casa.append(cosa('Estereo',2,1200))
casa.append(cosa('Celular Nokia',1,2500))
casa.append(cosa('Guitarra',1,1600))
casa.append(cosa('Wii',2,4500))
casa.append(cosa('Sombrero',1,600))
casa.append(cosa('reloj',1,900))
casa.append(cosa('VAJILLA',2,800))
casa.append(cosa('Los relojes Blandos. Dalí',1,1500))
casa.append(cosa('Calendario Maya',5,2100))
#casa.append(cosa('DVD',3,1000))
#casa.append(cosa('Busto Platón',2,3000))
#casa.append(cosa('Adorno',1,400))
def evalua(arreglo, combActual, limite):
    sumaValor = 0
    sumaPeso = 0
    for c in range(len(combActual)):
        if (combActual[c]=="1"):
            sumaValor = sumaValor+arreglo[c].valor
            sumaPeso = sumaPeso+arreglo[c].peso
    if (sumaPeso>limite):
        return -1
    else:
        return sumaValor
def comb2texto(comb,arreglo):
    texto = ""
    for c in range (len (comb)):
        if (comb[c] == "1"):
            texto=texto+" "+arreglo[c].nombre
    return texto

mejorC = 0
mayorG = 0
inicio=time.time()
for c in range(2**len(casa)):
    actual=bin(c)[2:]
    actual=actual.zfill(len(casa))
    ganancia = evalua(casa, actual, 10)
    if (ganancia>mayorG):
        mayorG = ganancia
        mejorC = actual
fin=time.time()
print(mejorC, mayorG)
print(fin-inicio," segundos") """

import time

def cumple(a,b,c,d,e,f,g,h):
    if((a+b+6)==c) and ((b+6+c)==d) and ((6+c+d)==11) and ((c+d+11)==e) and ((d+11+e)==f) and ((11+e+f)==g) and ((e+f+g)==h) and ((f+g+h)==14):
        return True
    else:
        return False

inicio = time.time()
e=16
for a in range(108, 115):
    for b in range (-200, 200):        
        for c in range(-200, 200):            
            d=5-c            
            f=d+27
            g = 27 + f
            h = 16 + f + g
            #actual = time.time()
            #print(actual - inicio)
            if cumple(a,b,c,d,e,f,g,h):
                print(a,b,c,d,e,f,g,h)    