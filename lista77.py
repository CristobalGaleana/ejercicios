nombre1= input("introduce el nombre de alguien a quien quieras invitar a la fiesta")
nombre2= input("introduce otro nombre")
nombre3= input("introduce un tercer nombre")
fiesta= [nombre1,nombre2,nombre3]
otro=("quieres rnvitar a alguien mas a la fiesta? (si o no):")
while otro == "si":
    nuevonombre= fiesta.append(input("introduce el otro nombre"))
    otro= input("quieres rnvitar a alguien mas a la fiesta? (si o no):")
    print("tienes",len(fiesta), invitados en tu fiesta)
    print (party)
    seleccion=("introduce uno de los nombres")
    print(seleccion,"esta en posicion",party.index(seleccion), "en la lista")
    aun=("aun quieres que ellos vengan? (si-no)")
    if aun == "n":
        party.remove(seleccion)
        print(fiesta)