class Neurona:
    entradas = []
    pesos = []
    umbral = 2
    salida = 0
    

    def __init__(self, e, w, u):
        self.entradas = e
        self.pesos = w
        self.umbral = u

    def evalua(self):
        suma = 0        
        for c in range(len(self.entradas)):
            suma = suma + self.entradas[c]*self.pesos[c]
        if (suma >= self.umbral):
            return 1
        else:
            return 0
"""entradas = [0,0]
print(entradas)
n1 = Neurona(entradas, [2,2], 2) #OR
n2 = Neurona(entradas, [1,1], 2) #AND
print("Neurona 1:", n1.evalua())
print("Neurona 2:", n2.evalua())"""

datos=[]
datos.append ("00001000000000100000000010000000001000000000100000"\
              "00001000000000100000000010000000001000000000100000")

umbral=2 
neuEntrada=[]
for cn in range(10):
    dato= datos[0]
    ent=[]
    cad=dato[cn*10:cn*10+10]
    for ce in range(10):
        ent.append(cad[ce])
    neuEntrada.append(Neurona(dato[cn*10:cn*10+10],[],umbral))             
        