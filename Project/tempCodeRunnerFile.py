import turtle as tu

# Setup screen
tu.title("Lord Hanuman Symbolic Art")
tu.bgcolor("black")
pen = tu.Turtle()
pen.speed(10)
pen.pensize(2)
pen.color("orange")

# Draw circular aura (symbolic halo)
pen.penup()
pen.goto(0, -200)
pen.pendown()
pen.begin_fill()
pen.circle(200)
pen.end_fill()

# Draw gada (mace) outline
pen.penup()
pen.goto(100, -50)
pen.pendown()
pen.color("gold")
pen.begin_fill()
pen.circle(40)
pen.end_fill()

pen.penup()
pen.goto(100, -10)
pen.pendown()
pen.pensize(10)
pen.goto(100, 180)

# Decorative bands on gada
pen.pensize(3)
pen.penup()
pen.goto(80, 120)
pen.pendown()
pen.goto(120, 120)

pen.penup()
pen.goto(80, 60)
pen.pendown()
pen.goto(120, 60)

# Symbolic face outline (simple curves)
pen.color("orange red")
pen.pensize(5)
pen.penup()
pen.goto(-150, 50)
pen.setheading(-30)
pen.pendown()
pen.circle(200, 60)

pen.penup()
pen.goto(-150, 50)
pen.setheading(30)
pen.pendown()
pen.circle(-200, 60)

# Tilak symbol
pen.color("white")
pen.pensize(8)
pen.penup()
pen.goto(-20, 100)
pen.pendown()
pen.goto(-20, 160)
pen.penup()
pen.goto(20, 100)
pen.pendown()
pen.goto(20, 160)
pen.penup()
pen.goto(0, 80)
pen.pendown()
pen.circle(10)

pen.hideturtle()
tu.done()
