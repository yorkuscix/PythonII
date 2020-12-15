import turtle
turtle.speed(0)

def drawBox(x, y):
    
    turtle.penup()
    turtle.setpos(x, y)
    turtle.pendown()

    turtle.color("red")
    turtle.begin_fill()
    turtle.setpos(x+87, y+50)
    turtle.setpos(x+87, y+150)
    turtle.setpos(x, y+100)
    turtle.setpos(x, y)
    turtle.end_fill()

    turtle.color("blue")
    turtle.begin_fill()
    turtle.setpos(x-87, y+50)
    turtle.setpos(x-87, y+150)
    turtle.setpos(x, y+100)
    turtle.setpos(x, y)
    turtle.end_fill()
    
    turtle.penup()
    turtle.setpos(x, y+100)
    turtle.pendown()
    
    turtle.color("green")
    turtle.begin_fill()
    turtle.setpos(x+87, y+150)
    turtle.setpos(x, y+200)
    turtle.setpos(x-87, y+150)
    turtle.setpos(x, y+100)
    turtle.end_fill()

def draw_3d_x(x):
    draw_box(x*87,x*(-50))

def draw_3d_y(y):
    draw_box(y*(-87),y*(-50))

def draw_3d_z(z):
    draw_box(0,z*100)

def drawBox3D(x, y, z):

    # Convert 3D point to 2D point
    x2D = 87*x - 87*y
    y2D = 100*z - 50*x - 50*y

    drawBox(x2D, y2D)

# drawing boxes with 3D coordinates

drawBox3D(0, 0, 0)
drawBox3D(1, 0, 0)
drawBox3D(0, 1, 0)
drawBox3D(0, 0, 1)
drawBox3D(3, 0, 1)

