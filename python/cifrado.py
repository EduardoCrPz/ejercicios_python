def cargaPalabras():
    archivo = open("words.txt", "r")
    texto = archivo.read()
    datos = texto.split()
    archivo.close()
    return (datos)

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
alfabeto = "abcdefghijklmnopqrstuvwxyz"
cifrado = "dciecih nza cmyi czgeiv cmhhn ozeeih jzyki jmhmeczrg jzhi "\
          "ekjig ecmr nza qmr qzarezh cmyi himv imqc zs eci"\
          " nza qmr qzarezh cmyi himv imqc zs eci giyir uzzpg zr "\
          "jzhi ecmr zri zqqmgkzr, ozeeihcimvg przd ecihi mhi gzji"\
          " qwmggkq wkrig ecme dkww mwdmng gemn dkec nza."

letras = {}
for c in alfabeto: #se crea e inicializa el diccionario "letras"
    letras[c] = 0
for c in alfabeto:
    letras[c]=cifrado.count(c)

archivo = open("salida.csv", "w")
for c in letras.keys():
    archivo.write(c+","+str(letras[c])+"\n")
archivo.close()

dic1 = cargaPalabras()
cont = 0
'''
#probando con qwmggkq

for pal in dic1:
    if (len(pal)==7):
        if (pal[0]==pal[-1]) and (pal[3]==pal[4]):
            cont = cont + 1
            print(pal)
'''


posQ="c"
posG="s"
posZ="o"
posR="n"
posK="i"
posI="e"
posY="mv"
posD="w"
posC="h"
posE="t"
posH="r"
posV="dl"
'''
#probando con zqqmgkzr
for pal in dic1:
    if (len(pal)==8):
        if (pal[0]==pal[-2]) and (pal[1]==pal[2]):
            if (pal[1] in posQ):
                cont = cont + 1
                print(pal)
print(cont)

#probando con jmhmeczrg
for pal in dic1:
    if (len(pal)==9):
        if (pal[1]==pal[3]):
            if (pal[-1] in posG) and (pal[-2] in posR):
                if (pal[-3] in posZ):
                    cont = cont + 1
                    print(pal)
print(cont)


#probando con qwmggkq
#             classic

for pal in dic1:
    if (len(pal)==7):
        if (pal[0]==pal[-1]) and (pal[3]==pal[4]):
            if(pal[0]=="c"):
                cont = cont + 1
                print(pal)
print(cont)


#probando con wkrig
#             linXs

for pal in dic1:
    if (len(pal)==5):
        if(pal[0]=="l") and (pal[1]=="i"):
            if(pal[2]=="n") and (pal[-1]=="s"):
                cont = cont + 1
                print(pal)
print(cont)
'''#probando con giyir
#                seXen

for pal in dic1:
    if (len(pal)==5):
        if(pal[0]=="s") and (pal[-1]=="n"):
            if(pal[1] in posI):
                if(pal[1]==pal[3]):
                    cont = cont + 1
                    #print(pal)
#print(cont)
    #28/09
"""#probando con dciecih
for pal in dic1:
    if (len(pal)==7):
        if(pal[1]==4) and (pal[2]==5):
            if(pal[2]=="e"):
                cont= cont+1
                
                print(pal)
print(cont)"""

#probando pnzw
for pal in dic1:
    if (len(pal)==4):
        if(pal[2:]=="ow"):
            cont=cont+1 
        print(pal)
print(cont)        
alfabeto= "abcdefghijklmnopqrstuvwxyz"
llave=    "xxxxxxxxxxxxxxxxxxxxxxxxxx"
texto= descifraSustituye(cifrado,llave)
print(texto)