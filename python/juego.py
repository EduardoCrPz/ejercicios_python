"""import random
opciones=[0,1,2]
cabinas=[]
def creaConcurso():
    cab=[]
    for c in range(3):
        cab.append(0)
    ale=random.choice(opciones) 
    cab[ale]=1
    return cab
def cabDescartar(cabinas, eleccion):
    vacias=[]
    for c in range(3):
        if (cabinas[c]==0):
            vacias.append( c)
    if(elec in vacias):
        vacias.remove(elec)
        return[0]
    else:
        return random.choice(vacias)    
n=10000
aciertos=0
for cs in range(n):
    cabinas=creaConcurso()
    elec=random.choice(opciones)
    descartar=cabDescartar(cabinas,elec)
    cambio=[0,1,2]
    cambio.remove(elec)
    nuevaElec=cambio[0]
    if (cabinas[elec]==1):    
        aciertos+=1

print(aciertos/n)       


n = 1000
aciertos = 0
for cs in range(n):
    cabinas=creaConcurso()
    elec = random.choice(opciones)
    descartar = cabDescartar(cabinas, elec)
    if (cabinas[elec]==1):
        aciertos+=1
print(aciertos/n)"""


