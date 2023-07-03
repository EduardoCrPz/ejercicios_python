import random
    

def evalua (ind):
    x= int(ind[0:3],2)
    y= int(ind[3:6],2)
    z= int(ind[6:],2)
    return x+y+z

numInd =10
poblacion = []
for c in range(9):
        ind = ind+ random.choice(["0","1"])
        cal= evalua(ind)
