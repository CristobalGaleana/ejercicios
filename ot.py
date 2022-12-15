import turtle
turtle.shape ("turtle")
turtle.color("black", "red")
scr=turtle.Screen()
#scr.bgcolor("yellow")

#turtle.pencolor(255,0,0)
#Pentagono
for i in range(0,5):
    turtle.forward(100)
    turtle.right(72)

turtle.penup()
turtle.forward(200)
turtle.pendown()


#cuadrado
for i in range (0,4):
    turtle.forward(50)
    turtle.left(90)


