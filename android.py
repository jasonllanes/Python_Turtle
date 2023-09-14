import turtle

ts = turtle.getscreen()
t = turtle.Turtle()


t.begin_fill()
t.fillcolor("#3DDC84")
t.penup()
t.forward(150)
t.pendown()
t.left(90)

t.speed(8)
for i in range(238):
 t.left(0.76)
 t.forward(1)


t.forward(100)

t.left(90)
t.forward(150)

t.left(90)
t.forward(100)

t.end_fill()

t.penup()
t.home()

t.penup()
t.goto(50,30)
t.pendown()
t.begin_fill()
t.fillcolor("white")
t.circle(15)
t.end_fill()

t.penup()
t.goto(100,30)
t.pendown()
t.begin_fill()
t.fillcolor("white")
t.circle(15)
t.end_fill()

t.penup()
t.home()
t.pendown()


t.left(270)

t.begin_fill()
t.fillcolor("#3DDC84")
for i in range(45):
 t.right(4)
 t.forward(1)
t.forward(70)
for i in range(45):
 t.right(4)
 t.forward(1)
t.forward(70)
t.end_fill()

t.penup()
t.goto(160,0)
t.pendown()

t.left(270)

t.begin_fill()
t.fillcolor("#3DDC84")
for i in range(45):
 t.right(4)
 t.forward(1)
t.forward(70)
for i in range(45):
 t.right(4)
 t.forward(1)
t.forward(70)
t.end_fill()

t.penup()
t.goto(30,-100)
t.pendown()

t.left(270)

t.begin_fill()
t.fillcolor("#3DDC84")
for i in range(45):
 t.right(4)
 t.forward(1)
t.forward(70)
for i in range(45):
 t.right(4)
 t.forward(1)
t.forward(70)
t.end_fill()

t.penup()
t.goto(100,-100)
t.pendown()


t.begin_fill()
t.fillcolor("#3DDC84")
for i in range(45):
 t.right(4)
 t.forward(1)
t.forward(70)
for i in range(45):
 t.right(4)
 t.forward(1)
t.forward(70)
t.end_fill()






