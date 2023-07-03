import random
import time

n = 1350
a = []
while (len(a)<n):
    ale = random.randint(0,n)
    if not(ale in a):
        a.append(ale)

inicio = time.time()
for d in range(len(a)):
    for c in range(len(a)-1):
        if (a[c]>a[c+1]):
            temp=a[c]
            a[c]=a[c+1]
            a[c+1]=temp
fin = time.time()
print("se tardó: ",fin-inicio)
        
