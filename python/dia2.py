#programa que determina si un valor entero es negativo o positivo 
a=int(input("Dime un numero entero: "))

if a>0:  """solo es en la primera condicion"""
    print(a,"a es un numero positivo")

elif a==0: """en la segunda condicion o intermedias"""
    print(a,"es cero")

else:   """solo se puede usar cuando ya es la ultima negacion"""
    print(a,"es un numero negativo")

"""if a>0: or a==0:
    print(a,"es un numero positivo o el elemento neutro ")
else:
    print(a,"es un numero negativo" ) """   