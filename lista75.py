numeros= [123,345,234,765]
for i in numeros:
    print (i)
seleccion= int(input("introduce un numero de la lista:"))
if seleccion in numeros:
    print(seleccion,"esta en posicion", numeros.index(seleccion))
else:
    print("ese numero no esta en la lista")