"""
a={}
a["a"]="lunes"
a["b"]="martes"
a["c"]="miercoles"
a["d"]="jueves"
a["e"]="viernes"
b=[]
b.append("lunes")
b.append("martes")
b.append("miercoeles")
b.append("jueves")
b.append("viernes")"""

def cargaPalabras():
    archivo = open("words.txt", "r")
    texto = archivo.read()
    datos = texto.split()
    archivo.close()
    return (datos)
alfabeto = "abcdefghijklmnopqrstuvwxyz"
cifrado = "dciecih nza cmyi czgeiv cmhhn ozeeih jzyki jmhmeczrg jzhi "\
          "ekjig ecmr nza qmr qzarezh cmyi himv imqc zs eci"\
          " nza qmr qzarezh cmyi himv imqc zs eci giyir uzzpg zr "\
          "jzhi ecmr zri zqqmgkzr, ozeeihcimvg przd ecihi mhi gzji"\
          " qwmggkq wkrig ecme dkww mwdmng gemn dkec nza."
letras={}
for c in alfabeto:   # se crea e inicializa el diccionario de letras 
    letras[c]=0
    #print(letras) 
for c in alfabeto:
    letras[c]=cifrado.count(c)
#print(letras)    
"""archivo=open("salida.csv","w")
for c in letras.keys():
    archivo.write(c+","+str(letras[c])+"\n")
archivo.close"""    

dic1=cargaPalabras()
cont=0
for pal in dic1:
    if(len(pal)==7):
        if( pal[0]==pal[-1])and(pal[3]==pal[4]):
            cont= cont +1
       # print(pal)"""
posQ="c" 
posG="s"
posZ="e"
posR="n"
posK="ci"       
posW="l"
posM="a"
posI="e"
posY="mw"
"""
for pal in dic1:
    if(len(pal)==8):
        if( pal[0]==pal[-2])and(pal[2]==pal[2]):
            if(pal[1]in posQ):
                cont = cont +1
        print(pal)
print(cont)        """
""" #probando wkrig

for pal in dic1:
    if(len(pal)==5):
        if( pal[0]=="l"[-1])and(pal[1]=="i"):
            if(pal[2]=="n" and pal[-1]=="s"):
                cont = cont +1
        print(pal)
print(cont)  """

#probando giyir

for pal in dic1:
    if(len(pal)==5):
        if( pal[0]=="s"[-1])and(pal[1]=="n"):
            if(pal[1] in posI):
                if(pal[])
                cont = cont +1
        print(pal)
print(cont)  