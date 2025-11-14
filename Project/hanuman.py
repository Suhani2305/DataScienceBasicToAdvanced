import turtle
import math

# --- Setup ---
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("lightyellow")
t = turtle.Turtle()
t.speed(0) # Fastest speed
t.hideturtle()
t.pensize(2)

# Function to draw a filled circle
def draw_filled_circle(x, y, radius, fill_color, border_color="black"):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.color(border_color, fill_color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Function to draw an oval (simplified by stretching a circle)
def draw_oval(x, y, x_radius, y_radius, fill_color, border_color="black"):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(border_color, fill_color)
    t.begin_fill()
    t.setheading(0)
    t.left(90) # Orient for drawing horizontal oval from center
    t.circle(x_radius, 90) # Quarter circle
    t.left(90)
    t.circle(y_radius, 90) # Quarter circle
    t.left(90)
    t.circle(x_radius, 90) # Quarter circle
    t.left(90)
    t.circle(y_radius, 90) # Quarter circle
    t.end_fill()


# Function to draw the Gada (Mace)
def draw_gada_detailed(x, y, scale=1):
    t.penup()
    t.goto(x, y)
    t.setheading(90) # Pointing up
    t.pendown()
    t.color("saddlebrown", "goldenrod")
    t.pensize(2)

    # Handle (bottom)
    t.begin_fill()
    t.right(90)
    t.forward(5 * scale)
    t.left(90)
    t.forward(20 * scale)
    t.left(90)
    t.forward(10 * scale)
    t.left(90)
    t.forward(20 * scale)
    t.left(90)
    t.forward(5 * scale)
    t.end_fill()

    t.penup()
    t.goto(x, y + 20 * scale)
    t.pendown()

    # Main staff
    t.setheading(90)
    t.color("brown")
    t.forward(80 * scale)

    # Top head of the Gada (more spiky)
    t.penup()
    t.goto(x, y + 100 * scale)
    t.pendown()
    t.color("black", "gold")
    t.begin_fill()
    t.right(90)
    t.forward(15 * scale)
    for _ in range(4): # Spikes
        t.left(120)
        t.forward(10 * scale)
        t.right(60)
        t.forward(10 * scale)
        t.right(120)
        t.forward(15 * scale)
        t.right(90)
    t.end_fill()


# Function to draw the meditating figure (more detailed)
def draw_meditating_figure(x, y, scale=1):
    
    # Orange Dhoti/Robe
    t.penup()
    t.goto(x, y - 10 * scale)
    t.pendown()
    t.color("black", "darkorange")
    t.begin_fill()
    t.setheading(270) # Down
    t.circle(80 * scale, 180) # Bottom curve of legs
    t.setheading(90) # Up
    t.forward(50 * scale) # Torso side
    t.setheading(0)
    t.forward(10 * scale) # Small flat for waist
    t.setheading(90)
    t.forward(50 * scale) # Torso other side
    t.end_fill()

    # Skin color for arms/shoulders (simplified)
    t.penup()
    t.goto(x - 50 * scale, y + 40 * scale)
    t.pendown()
    t.color("black", "tan")
    t.begin_fill()
    t.setheading(90)
    t.circle(20 * scale, 180) # Left arm curve
    t.setheading(270)
    t.forward(10 * scale)
    t.setheading(0)
    t.forward(80 * scale)
    t.setheading(90)
    t.forward(10 * scale)
    t.circle(20 * scale, 180) # Right arm curve
    t.end_fill()


    # Head (more like a rounded square/oval for a monkey face)
    draw_filled_circle(x, y + 100 * scale, 35 * scale, "tan")
    
    # Hair
    t.penup()
    t.goto(x - 15 * scale, y + 130 * scale)
    t.pendown()
    t.color("black", "brown")
    t.begin_fill()
    t.setheading(45)
    t.circle(20 * scale, 90)
    t.setheading(225)
    t.circle(20 * scale, 90)
    t.end_fill()

    # Tilak on forehead
    t.penup()
    t.goto(x - 5 * scale, y + 115 * scale)
    t.pendown()
    t.color("red")
    t.setheading(90)
    t.forward(10 * scale)
    t.right(90)
    t.forward(10 * scale)
    t.right(90)
    t.forward(10 * scale)
    
    # Hands in Namaste pose (very simplified)
    t.penup()
    t.goto(x + 5 * scale, y + 10 * scale) # Approx center of chest
    t.pendown()
    t.color("black", "tan")
    t.begin_fill()
    t.setheading(180) # Facing left
    t.forward(15 * scale)
    t.right(90)
    t.forward(20 * scale)
    t.right(90)
    t.forward(30 * scale)
    t.right(90)
    t.forward(20 * scale)
    t.right(90)
    t.forward(15 * scale)
    t.end_fill()

    # Tail (simple curve)
    t.penup()
    t.goto(x + 80 * scale, y - 50 * scale)
    t.pendown()
    t.color("brown")
    t.setheading(45)
    t.circle(50 * scale, -90)
    t.setheading(135)
    t.circle(20 * scale, -90)
    t.dot(10, "brown") # End of tail


# --- Drawing Commands ---

# 1. Background Halo/Moon
draw_filled_circle(0, 50, 120, "paleturquoise", "none")
draw_filled_circle(0, 50, 115, "lightyellow", "none") 

# 2. Meditating Figure
draw_meditating_figure(0, -100, scale=1.0)

# 3. Gada (Mace)
draw_gada_detailed(-180, -120, scale=1.0) # Positioned to the left

# --- Finish ---
t.penup()
t.goto(0, 250)
t.color("darkblue")
t.write("My Turtle Art: Meditating Figure", align="center", font=("Arial", 20, "bold"))

screen.mainloop()