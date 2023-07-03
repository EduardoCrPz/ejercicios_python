"""
import random
import time

n = 13500
a = []
while (len(a)<n):
    ale = random.randint(0,n)
    if not(ale in a):
        a.append(ale)
mitad = n // 2
inferior = []
superior = []
inicio = time.time()
for e in a:
    if (e<mitad):
        inferior.append(e)
    else:
        superior.append(e)
#print(inferior)
#print(superior)
for cont in range(len(inferior)):
    for c in range(len(inferior)-1):
        if (inferior[c]>inferior[c+1]):
            temp=inferior[c]
            inferior[c]=inferior[c+1]
            inferior[c+1]=temp
for cont in range(len(superior)):
    for c in range(len(superior)-1):
        if (superior[c]>superior[c+1]):
            temp=superior[c]
            superior[c]=superior[c+1]
            superior[c+1]=temp
fin = time.time()
#print(inferior)
#print(superior)
#print("se tardó: ",fin-inicio)
print(a.sort)"""


#snapback


