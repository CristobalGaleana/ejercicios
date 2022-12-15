listaAlumnos = [] #lista vacia
respuesta= "si"

while respuesta =="si":
    listaAlumnos.append(input("Agrega el nombre del alumno: ")) #agrega elementos al ultimo de la lista
    print(listaAlumnos)

    respuesta=input("Escriba si, para agregar otro alumno a la lista: ")

listaAlumnos.sort()#ordena la lista pero no funciona cuando tienes varios datos de diferentes tipos
print(listaAlumnos)