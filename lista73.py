comida_eleccion= {}
comida1=input("introduce una comida que te guste")
comida_eleccion[1]= comida1
comida2=input("introduce otra comida que te guste")
comida_eleccion[2]= comida2
comida3= input("una tercera comida que te guste")
comida_eleccion[3]= comida3
comida4= ("introduce una ultima comida que te guste")
comida_eleccion[4]= comida4
print(comida_eleccion)
nogusta= int(input("de que comida te quieres deshacer"))
del comida_eleccion[nogusta]
print(sorted(comida_eleccion.values()))