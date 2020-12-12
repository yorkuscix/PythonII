import turtle

turtle.penup()
turtle.setpos(0, 0)
turtle.pendown()

turtle.color("green")
turtle.begin_fill()
turtle.setpos(87, 50)
turtle.setpos(87, 150)
turtle.setpos(0, 100)
turtle.setpos(0, 0)
turtle.end_fill()

turtle.color("grey")
turtle.begin_fill()
turtle.setpos(-87, 50)
turtle.setpos(-87, 150)
turtle.setpos(0, 100)
turtle.setpos(0, 0)
turtle.end_fill()

turtle.penup()
turtle.setpos(0, 100)
turtle.pendown()

turtle.color("orange")
turtle.begin_fill()
turtle.setpos(87, 150)
turtle.setpos(0, 200)
turtle.setpos(-87, 150)
turtle.setpos(0, 100)
turtle.end_fill()