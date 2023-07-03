def izquierda(a,b):
    return a < b

def derecha(a,b):
    return b > a

def valida(casas):
    c1 = False
    c2 = False
    c3 = False
    #c4 = False
    c5 = False
    c6 = False
    c7 = False
    c8 = False
    c9 = False
    #c10 = False
    c11 = False
    c12 = False
    c13 = False
    c14 = False
    c15 = False
   
    for cas in casas:
        if (cas.nacionalidad=="britanico"):
            if (cas.nacionalidad == "roja"):
                c1 = True
    for cas in casas:
        if (cas.nacionalidad=="sueco"):
            if (cas.mascota == "perro"):
                c2 = True
    for cas in casas:
        if (cas.nacionalidad == "danes"):
            if (cas.bebida == "te"):
                c3 = True
    for cas in casas:
        if (cas.nacionalidad == "aleman"):
            if (cas.cigarros == "Prince"):
                c5 = True
    for cas in casas:
        if (izquierda(cas.color == "verde", cas.color == "blanca")):
            c6 = True
    for cas in casas:
        if (cas.color == "verde"):
            if (cas.bebida == "cafe"):
                c7 = True
    for cas in casas:
        if (cas.cigarros == "Pall Mall"):
            if (cas.mascota == "pajaros"):
                c8 = True
    for cas in casas:
        if (cas.color == "amarilla"):
            if (cas.cigarros == "Dunhill"):
                c9 = True
    for cas in casas:
        if (izquierda(cas.cigarros == "Blends", cas.mascota == "gato") or derecha(cas.cigarros == "Blends", cas.mascota == "gato")):
            c11 = True
    for cas in casas:
        if (izquierda(cas.mascota == "caballo", cas.cigarros == "Dunhill") or derecha(cas.mascota == "caballo", cas.cigarros == "Dunhill")):
            c12 = True
    for cas in casas:
        if (cas.cigarros == "Bluemaster"):
            if (cas.bebida == "cerveza"):
                c13 = True
    for cas in casas:
        if (izquierda(cas.cigarros == "Blends", cas.bebida == "agua") or derecha(cas.cigarros == "Blends", cas.bebida == "agua")):
            c14 = True
    #for cas in casas:
     #   if(izquierda(casas[0], cas.color == "azul") or derecha(cas[0], cas.color == "azul")):
      #      c15 = True
    
    
    if (c1 and c2 and c3 and c5 and c6 and c7 and c8 and c9 and c11 and c12 and c13 and c14):
        return True
    else:
        return False

print()        