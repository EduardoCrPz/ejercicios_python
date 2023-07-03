def cargaPalabras():
    archivo= open("wordsi.txt","r")
    texto=archivo.read()
    datos=texto.split()
    archivo.close()
    return(datos)
alfabeto="abcdefghijklmnopqrstuvwxyz"
cifrado="mc qp ksgys dsxhs gsbqnhs, ax ksxxs xqpls e ap lgcp ycghe pqos, xc henhc yakksxc e yachhc, ax bekks ogahhs, shhqns, ysks cggshspochs pexxc ycghe cphegasge e yachhs ap yqphc; xe dcnkexxe nsps yaelmejsxa e na nycxcpkcps ap qps nzqcgkas kme laqple fap nshhs x'skkmas, eo cxx'apkagkc cxxc dehc oa zqexxc nqyegasge na cygsps xe pcgaka, oajcgakche e yaqhhsnhs xqplme. lxa skkma nsps xqplma e xqkepha, ksp xc ycxyebgc nqyegasge ygsjjanhc oa kalxac, xe sgekkmae nsps pqoe, cyeghe, gajenhahe aphegpcdephe oa ygsoqiaspa faxafsgda, xe icdye cxhe e gsbqnhe, oex hqhhs pqoe, c ycghe cxkqpe nehsxe kme nyqphcps nqxxe ksnke. a hcgna nsps ksyegha oc xcglme nzqcde e xe icdye mcpps oqe oahc, x'aphegps fsgpahs oa qp fsghe cghalxas qnchs ksde sglcps sffepnajs pexxe xshhe hgc dcnkma s ksde oafenc pea kspfgspha oea ygeochsga"
letras = {}
dic1 = cargaPalabras()
cont= 0


posE = "e"
posS = "s"
posA = "i"
posC = "a"
posG = "r"
posP = "n"
posH = "m"
posN = "l"
posO = "d"
posX = "t"
posY = "f"
posK = "c"
posL = "m"
posM = "h"
posJ = "e"
posQ= "u"

"""

#prueba bekks

for pal in dic1:
    if(len(pal)== 6):
        if(pal[1] in posES) and (pal[-1] in posES):
            cont= cont+1
            print(pal)
print(cont)            



#prueba con  xe
for pal in dic1:
    if(len(pal)==2 ):
            if(pal[1] in posES):
                cont= cont+1
                print(pal)
print(cont)           

#prueba con cphegasge
for pal in dic1:
    if(len(pal)==9):
        if(pal[3]==pal[-1]):
            if(pal[3] in posES)and (pal[-3] in posES):
                if(pal[0] in posAC) and (pal[-4] in posAC):
                    cont = cont+1
                    print(pal)
print(cont)                


#provando con cggshspochs. Obtuve

for pal in dic1:
    if(len(pal) == 11):
        if(pal[0] == pal[-3]) and (pal[1] == pal[2]):
            if(pal[3] == pal[5]):
                if(pal[5] == pal[-1]) and (pal[3] == pal[-1]):
                    if(pal[4] == pal[-2]):
                        cont = cont + 1
                        print(pal)
print(cont)
"""
#Provando con yaelmejsxa
              #firmeresti
for pal in dic1:
    if(len(pal) == 10):
        if(pal[0] == "f") and (pal[1] == pal[-1]) and (pal[2] == pal[5]) and (pal[-2] in posX):
            cont = cont + 1
            print(pal)
print(cont)

       
    
