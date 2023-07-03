arch = open("salida.bmp", "rb")
datos = arch.read()
arch.close()

tamanio="0b"
for c in range(24):
    d = datos[54+c]
    valor = str(bin(d))
    print(valor)
    tamanio += valor[-1]
tamanio = int(tamanio, 2)

datos2 = []
for c in range(tamanio):
    byteGuardado = "0b"
    for c2 in range(8):
        d = datos[78+c*8+c2]
        d = str(bin(d))
        byteGuardado+=d[-1]
    datos2.append(int(byteGuardado, 2))

datos2 = bytes(datos2)
arch = open("algo.jpg", "wb")
arch.write(datos2)
arch.close()
            
"""
print("tamaño de la información a esconder", tamanio)
if(tamMax>tamanio):
    tamanio = bin(tamanio)[2:].zfill(24)
    print(tamanio)
    datos3 = []
    for c in range(54): #cabecera BMP
        datos3.append(datos[c])
    
    for c in range(len(datos2)):
        byteAguardar= str(bin(datos[c]))[2:].zfill(8)  
        for c2 in range(8):
            d = datos[78+c*8+c2]
            valor = str(bin(d))   
            valor = valor[:-1]+byteAguardar[c2]
            #valor = "0b"+byteAguardar[c2]+valor[3:]
            datos3.append(int(valor,2))
    for c in range(len(datos)-78- len(datos2)*8):
        datos3.append(datos[c+78+len(datos2)*8])
    datos3 = bytes(datos3)
    arch = open("salida.bmp", "wb")
    arch.write(datos3)
    arch.close()
            
else:
    print("la información no cabe")"""