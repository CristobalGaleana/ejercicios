tv=("taskmaster","top gear", "big bang theory", "how i met your mother")
for i in tv:
    print (i)
print()
nuevatv= ("introduce otro programa de televivsion")
posicion = int(input("introduce un numero entre 0 y 3:"))
tv.insert(posicion,nuevatv)
for i in tv:
    print (i)