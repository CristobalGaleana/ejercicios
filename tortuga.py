import turtle

turtle.shape("turtle")
turtle.color("black","red")
scr = turtle.Screen()
#scr.bgcolor("yellow")

turtle.pencolor("purple")


numeroLados = int(input("Ingresa el número de lados que quieres: "))


for i in range(0,numeroLados):
    turtle.forward(10)
    turtle.right(360/numeroLados)


turtle.penup()
turtle.forward(200)
turtle.pendown()

#cuadrado
for i in range(0,4):
    turtle.forward(50)
    turtle.left(90)
    


turtle.pencolor("green")

for i in range(0,10):
    turtle.right(36)
    for i in range(0,5):
        turtle.forward(100)
        turtle.right(72)

turtle.exitonclick()