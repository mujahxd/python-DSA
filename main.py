import turtle as t

t.title("Doraemon Full Body")
t.bgcolor("white")
t.speed(0)
t.pensize(3)

# --- Kepala Biru ---
t.penup()
t.goto(0, -180)
t.pendown()
t.color("blue")
t.begin_fill()
t.circle(180)
t.end_fill()

# --- Wajah Putih ---
t.penup()
t.goto(0, -150)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(150)
t.end_fill()

# --- Mata ---
for x in [-35, 35]:
    t.penup()
    t.goto(x, 80)
    t.pendown()
    t.color("white")
    t.begin_fill()
    t.circle(30)
    t.end_fill()

for x in [-35, 35]:
    t.penup()
    t.goto(x, 95)
    t.pendown()
    t.color("black")
    t.begin_fill()
    t.circle(10)
    t.end_fill()

# --- Hidung ---
t.penup()
t.goto(0, 60)
t.pendown()
t.color("red")
t.begin_fill()
t.circle(15)
t.end_fill()

# --- Mulut ---
t.penup()
t.goto(-60, 10)
t.setheading(-60)
t.pendown()
t.color("black")
t.pensize(3)
t.circle(70, 120)

# --- Kumis ---


def kumis(x, y, angle):
    t.penup()
    t.goto(x, y)
    t.setheading(angle)
    t.pendown()
    t.forward(60)


for y in [40, 20, 0]:
    kumis(-70, y, 180)
    kumis(70, y, 0)

# --- Badan ---
t.penup()
t.goto(-90, -180)
t.pendown()
t.color("blue")
t.begin_fill()
t.goto(-90, -350)
t.goto(90, -350)
t.goto(90, -180)
t.end_fill()

# --- Perut Putih ---
t.penup()
t.goto(0, -200)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(100)
t.end_fill()

# --- Saku ---
t.penup()
t.goto(-50, -200)
t.setheading(-90)
t.pendown()
t.pensize(3)
t.circle(50, 180)

# --- Kalung ---
t.penup()
t.goto(-90, -160)
t.pendown()
t.color("red")
t.pensize(15)
t.forward(180)

# --- Lonceng ---
t.penup()
t.goto(0, -170)
t.pendown()
t.color("yellow")
t.pensize(3)
t.begin_fill()
t.circle(20)
t.end_fill()
t.penup()
t.goto(0, -190)
t.setheading(-90)
t.pendown()
t.forward(10)

# --- Tangan ---


def tangan(x, y, mirror=False):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("blue")
    t.begin_fill()
    if mirror:
        t.setheading(200)
    else:
        t.setheading(-20)
    t.forward(60)
    t.circle(30, 180)
    t.forward(60)
    t.end_fill()


# kiri dan kanan
tangan(-90, -150, True)
tangan(90, -150, False)

# --- Kaki ---


def kaki(x):
    t.penup()
    t.goto(x, -350)
    t.pendown()
    t.color("white")
    t.begin_fill()
    t.circle(40)
    t.end_fill()


kaki(-60)
kaki(60)

t.hideturtle()
t.done()
