"""año= int(input("¿que año es este"))
edad= int(input("¿cuantos años tienes"))
cumpleaños= int(input("\n Ya fue tu cumpleaños? \n0 = no \n1 =si "))
nacimiento= año-edad-1+ cumpleaños 
print("\n su año de nacimiento es",nacimiento )"""



def esPalindromo(cadena):
    cadena=cadena.replace("","")
    longitud=len(cadena)
    if longitud %2==0:
        derecha=cadena[longitud//2:]
        izquierda=cadena[:longitud//2]
    
    else:
        derecha=cadena[longitud//2+1:]
        izquierda=cadena[:longitud//2] 
    
    return izquierda == derecha[::-1] 

print(esPalindromo("reconocer")) 
print(esPalindromo("amor a roma"))   

def esPar(num):
    if(num%2==0):
        return True
    else:
        return False  
print(esPar(11))        



def inverteCad(cadena):
    cadena=cadena.replace("")

    
def invierteCad(cadena):
    cad1=""

    for i in range(len(cadena)-1,-1,-1):
        cad1+= cadena[i]

    return cad1

cad1 = invierteCad(cadn)
cadn=input("Escriba el texto; ")

print("cadena normal:" , cadn)
print("cadena alrevez;" , cad1)