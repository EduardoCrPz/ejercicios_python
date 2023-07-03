def cargaPalabras():
    archivo= open("ingles.txt","r")
    texto=archivo.read()
    datos=texto.split()
    archivo.close()
    return(datos)
alfabeto="abcdefghijklmnopqrstuvwxyz"
cifrado="Gzt mtng kup gq oateidg gzt xsgsat in gq ivrtvg ig Gasng iv eatuyn, xqa iv gzty in zieetv gzt wugt gq tgtavigp Zuooivtnn in kztv kzug pqs gzivc, kzug pqs nup, uve kzug pqs eq uat iv zuayqvp  U yuv in msg gzt oaqesdg qx zin gzqswzgn kzug zt gzivcn, zt mtdqytn Ull qsa eatuyn duv dqyt gast ix kt zurt gzt dqsauwt gq osanst gzty Nsddtnn in vqg xivul, xuilsat in vqg xugul: ig in gzt dqsauwt gq dqvgivst gzug dqsvgn Wqqe gzivwn dqyt gq otqolt kzq kuig, msg mtggta gzivwn dqyt gq gzqnt kzq wq qsg uve wtg gzty"    


letras = {}
dic1 = cargaPalabras()

posGT = "et"

cont=0
"""
#provando con tgtavigp
for pal in dic1:
    if(len(pal) ==8):
        if(pal[0] == pal[2]) and(pal[1] == pal [-2]):
            if(pal[2] in posGT)and (pal[1]in posGT):
                cont = cont + 1
                print(pal)
print(cont)        
"""
#provando con gzt
for pal in dic1:
    if(len(pal) ==3):
        if(pal[0]) ==pal[2] and(pal[2] in posGT):
            cont=cont+1
            print(pal)
