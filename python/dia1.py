"""programa que pregunta mi nombre"""

"""el nombre es una cadena"""
"""
minombre= input("¿como te llamas?")
print("mucho gusto",minombre)
miedad= int(input("¿cual es tu edad "))

triple= 3*miedad
print ("\n \t \a el triple de tu edad actual es ",triple)"""

"""

for i in range(1,10):  
    print(i)
"""
"""
for i in range(10,0,-1):  
    print(i)"""

"""

for i in range(0,11,3):  
    print(i)  """  
"""

for i in range(10,-1,-2):  
    print(i)  """  

"""   
for i in "buenos dias":  
    print(i)    """

"""  
suma=0.0  
for i in range(10):  
    suma=suma+i
    print(i)   
print(suma)     """
"""
a= input("escribe el dato:")   #para convertir de cadena a intero y poder sumar
a=int(a)
b= input("escribe el 2 dato: ")
b=int(b)
print(a+b)
"""
"""
a= 4
b=2
print (a/b)"""

"""
a= 5
b=2
print (a/b)"""
"""
a= 5
b=2
print (a//b)"""
"""
a= 5
b=2
print (a%b)"""

"""    
(1-3)%12=10 

(1-3)%24=22""" # aritmetica modular

"""
import random
random.random()"""
"""
import random

opComp = random.randint(0,2)
print("opciones 0=piedra  1= tijera  2= papel")
opHumano=int(input("escribe la opcion"))
opComp=random.randint("la eleccion de la compu es",opComp)
if(opHumano==0) and (opComp==1):
    print("gana la computadora")
if(opHumano==1) and (opComp==1):
    print("empate")
if(opHumano==2) and (opComp==1):
    print("gana el humano")  """  
"""
import random   # piedra papel y tijer

opComp = random.randint(0,2)

opHumano = int(input("escribe opcion:"))
opComp = random.randint(0,2)
print("La eleccion de la compu es: ",opComp)
resultado = (opComp - opHumano) % 3
if (resultado==0):
    print("es un empate")
if (resultado==1):
    print("gana la computadora")
if (resultado==2):
    print("gana el humano")"""

"""
import random
def num2nom(num):
    if (num==0):
        return "piedra"
    elif (num==1):
        return "tijeras"
    elif (num==2):
        return "lagarto"
    elif (num==3):
        return "papel"
    elif (num==4):
        return "Spock"

print("opciones: \n0 = piedra \n1 = tijeras\n2 = lagarto")
print("3 = papel \n4 = Spock")
opHumano = int(input("escribe opcion:"))
opComp = random.randint(0,4)
print("la opción humana fue:",num2nom(opHumano))
print("La eleccion de la computadora es: ",num2nom(opComp))
resultado = (opHumano - opComp) % 5
if (resultado==0):
    print("es un empate")
else:
    if (resultado>2):
        print("ganaste!!!")
    else:
        print("gana la computadora!")

"""

"""def triple(algo):
    return(algo*3)        
print(triple(4))
print(triple(2.8))    
print(triple("hola "))"""

""" # slices 
a="este texto es una prueba"
a[1]
a[2]
a[3]
a[4]

#listas
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
print(a[::-1])"""

"""
def esPalindromeR(p):
    if(len(p)>2):
        return True
    elif(p[0]==p[-1]) and esPalindromeR(p[1:-1]):
        return True
    else:    
        return False    
print (esPalindromeR("hola"))"""

"""
from typing import Text
texto="hola"
print (alfabeto.index("v"))

for c in texto:
    pos= alfabeto.index(c)
    pos2=(pos+13)%26 
    print (c,pos,alfabeto[pos2])"""


"""

def cifraCesar(cad, llave):
    cad = cad.lower()
    cifrado = ""
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    for c in cad:
        if (c in alfabeto):
            pos = alfabeto.index(c)
            pos2 = (pos+llave)%26
            cifrado = cifrado + alfabeto[pos2]
        else:
            cifrado = cifrado + c
            
    return cifrado
for i in range(20):
    print(cifraCesar("hola a todos", i))

texto="buenos dias jovenes"
textoCifrado=cifraCesar(texto,5)
print(textoCifrado)
prueba=cifraCesar(textoCifrado,21)
print(prueba)

a='wklw wk wd lwplg imw lawfwf imw vwkumtjaj'
for i in range(25):
    print(cifraCesar(a,i)) """

def cifraSustituye (cad, llave):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    cad = cad.lower()
    cifrado = ""
    for c in cad:
        if (c in alfabeto):
            pos=alfabeto.index(c)
            cifrado=cifrado+llave[pos]
        else:
            cifrado=cifrado+c            
    return cifrado
def descifraSustituye (cad, llave):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    cad = cad.lower()
    texto = ""
    for c in cad:
        if (c in alfabeto):
            pos=llave.index(c)
            texto=texto+alfabeto[pos]
        else:
            texto=texto+c            
    return texto
texto = "la materia que mas me gusta es la de algoritmos porque "\
        "el profe Marcelo es el mejor"
llave = "piqdhrsltjgnokufmcavwxyzeb"
prueba = cifraSustituye (texto, llave)
print(prueba)
claro = descifraSustituye(prueba, llave)
print(claro)
def cifraCesar(cad, llave):
    cad = cad.lower()
    cifrado = ""
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    for c in cad:
        if (c in alfabeto):
            pos = alfabeto.index(c)
            pos2 = (pos+llave)%26
            cifrado = cifrado + alfabeto[pos2]
        else:
            cifrado = cifrado + c            
    return cifrado

def descifraCesar(cad, llave):
    cad = cad.lower()
    cifrado = ""
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    for c in cad:
        if (c in alfabeto):
            pos = alfabeto.index(c)
            pos2 = (pos-llave)%26
            cifrado = cifrado + alfabeto[pos2]
        else:
            cifrado = cifrado + c            
    return cifrado
def cifraSustituye (cad, llave):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    cad = cad.lower()
    cifrado = ""
    for c in cad:
        if (c in alfabeto):
            pos=alfabeto.index(c)
            cifrado=cifrado+llave[pos]
        else:
            cifrado=cifrado+c            
    return cifrado
def descifraSustituye (cad, llave):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    cad = cad.lower()
    texto = ""
    for c in cad:
        if (c in alfabeto):
            pos=llave.index(c)
            texto=texto+alfabeto[pos]
        else:
            texto=texto+c            
    return texto
texto = "la materia que mas me gusta es la de algoritmos porque "\
        "el profe Marcelo es el mejor"
llave = "piqdhrsltjgnokufmcavwxyzeb"
prueba = cifraSustituye (texto, llave)
print(prueba)
claro = descifraSustituye(prueba, llave)
print(claro)
def cifraCesar(cad, llave):
    cad = cad.lower()
    cifrado = ""
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    for c in cad:
        if (c in alfabeto):
            pos = alfabeto.index(c)
            pos2 = (pos+llave)%26
            cifrado = cifrado + alfabeto[pos2]
        else:
            cifrado = cifrado + c            
    return cifrado

def descifraCesar(cad, llave):
    cad = cad.lower()
    cifrado = ""
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    for c in cad:
        if (c in alfabeto):
            pos = alfabeto.index(c)
            pos2 = (pos-llave)%26
            cifrado = cifrado + alfabeto[pos2]
        else:
            cifrado = cifrado + c            
    return cifrado



def cargaPalabras():
    archivo=open("words.txt","r")
    texto = archivo.read()
    datos = texto.split()
    archivo.close()
    return (datos)

def getAciertos(cad, d):
    aciertos = 0
    texto1 = cad.split()
    for pal in texto1:
        if (pal in d):
            aciertos = aciertos + 1
    return aciertos

original = "Member states are expected to deliberate on two parallel"\
           "challenges: ending the Covid-19 pandemic and redefining"\
           "the post-pandemic global economy"
cifrado = cifraCesar(original, 17)
print("texto cifrado")
print (cifrado)
print()
dic1 = cargaPalabras()

maxAciertos = 0
llave = 0
for c in range(26):
    textoP = descifraCesar(cifrado , c)
    aciertos = getAciertos(textoP, dic1)
    if (aciertos>maxAciertos):
        maxAciertos = aciertos        
       
    llave = c
        
print("el texto buscado es:")
print(descifraCesar(cifrado , llave))   