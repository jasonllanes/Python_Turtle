import turtle


t = turtle.Turtle()
t.speed(10)
screen = turtle.Screen()
screen.listen() 

#movementes_functions
def move_left():
    t.penup()
    t.setheading(180)
    t.fd(100)

def move_right():
    t.penup()
    t.setheading(0)
    t.fd(100)

def move_up():
    t.penup()
    t.setheading(90)
    t.fd(100)

def move_down():
    t.penup()
    t.setheading(270)
    t.fd(100)

#square_function
def draw_square():
    t.begin_fill()
    t.fillcolor("Red")
    t.pendown()
    for i in range(4):
        t.fd(50)
        t.rt(90)
    t.end_fill()
    t.penup()

def draw_circle():
    t.begin_fill()
    t.fillcolor("#3DDC84")
    t.pendown()
    t.circle(50)
    t.end_fill()
    t.penup()

def draw_triangle():
    t.begin_fill()
    t.fillcolor("Orange")
    t.pendown()
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.end_fill()
    t.penup()

#Commands
screen.onkey(move_left, "Left");
screen.onkey(move_right, "Right");
screen.onkey(move_up, "Up");
screen.onkey(move_down, "Down");

screen.onkey(draw_square, "s");
screen.onkey(draw_circle, "c");
screen.onkey(draw_triangle, "t");

screen.onkey(pen_up, "1");
screen.onkey(pen_down, "2");




