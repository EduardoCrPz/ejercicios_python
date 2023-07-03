from _typeshed import Self


class grafo:
    def __init__(self,archivo):
        self.Nodos=[]
        self.Aristas=[]
        self.MatrizAdyacencia=[]
        lineas=[]
        with open(archivo,"r") as archivo:
            for linea in archivo:
                lineas.append(linea)
        for i in range(len(lineas)):
            lineas[i]=lineas[i].strip("\n")
            N = lineas[i].split ("->")
            self.Nodos.append(N[0])
            self.Nodos.append(N[1])
            self.Aristas([N[0],N[1]])
            self.Aristas([N[1],N[0]])         
        self.Nodos=list(set(self.Nodos))
        for i in range(len(self.Nodos)):
            fila=[]
            for j in range(len(self.Nodos)):
                fila.append(0)
            self.MatrizAdyacencia.append(fila)
        for e in self.Aristas:
            a=self.Nodos.index(e[0])
            b=self.Nodos.index(e[1])
            self.MatrizAdyacencia  
            
       
