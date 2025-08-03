import turtle

# --- Helper Functions ---

# Function to move the turtle without drawing
def move_to(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

# Function to draw and fill a rectangle (for the flag stripes)
def draw_rectangle(width, height, color):
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

# Function to draw the crossed spears
def draw_spears():
    turtle.color("white")
    turtle.pensize(8)

    # Draw spear shafts
    move_to(-80, 125)
    turtle.goto(80, -125)
    move_to(-80, -125)
    turtle.goto(80, 125)

    # Draw spear heads (triangles)
    turtle.pensize(1)
    # Top-right spear head
    move_to(80, 125)
    turtle.begin_fill()
    turtle.goto(70, 145)
    turtle.goto(90, 145)
    turtle.goto(80, 125)
    turtle.end_fill()

    # Top-left spear head
    move_to(-80, 125)
    turtle.begin_fill()
    turtle.goto(-70, 145)
    turtle.goto(-90, 145)
    turtle.goto(-80, 125)
    turtle.end_fill()

# Function to draw one of the shield's curved sides
def draw_shield_side(start_x, start_y, end_x, end_y):
    turtle.goto(start_x * 0.8, start_y * 0.6)
    turtle.goto(start_x, 0)
    turtle.goto(end_x * 0.8, end_y * 0.6)
    turtle.goto(0, end_y)

# Function to draw the complete Maasai shield with all details
def draw_the_shield():
    # 1. White border of the shield
    move_to(0, 105)
    turtle.color("white", "white")
    turtle.begin_fill()
    draw_shield_side(-55, 105, -55, -105) # Left side
    draw_shield_side(55, -105, 55, 105)  # Right side
    turtle.end_fill()

    # 2. Black base of the shield
    move_to(0, 100)
    turtle.color("black", "black")
    turtle.begin_fill()
    draw_shield_side(-50, 100, -50, -100) # Left side
    draw_shield_side(50, -100, 50, 100)  # Right side
    turtle.end_fill()

    # 3. Red panel in the middle
    move_to(0, 85)
    turtle.color("red", "red")
    turtle.begin_fill()
    draw_shield_side(-35, 85, -35, -85) # Left side of red panel
    draw_shield_side(35, -85, 35, 85)  # Right side of red panel
    turtle.end_fill()
    
    # 4. White central disc and decorative shapes
    move_to(0, 0)
    turtle.dot(35, "white") # Central disc

    # Four smaller shapes
    move_to(-15, 45)
    turtle.dot(12, "white")
    move_to(15, 45)
    turtle.dot(12, "white")
    move_to(-15, -45)
    turtle.dot(12, "white")
    move_to(15, -45)
    turtle.dot(12, "white")


# --- Main Drawing ---

# Setup screen
turtle.setup(width=800, height=500)
turtle.speed(3)
turtle.bgcolor("#f0f0f0")
turtle.title("Flag of Kenya")

# Flag dimensions
FLAG_WIDTH = 600
FLAG_HEIGHT = 400
FIMBRIATION_HEIGHT = FLAG_HEIGHT / 18 # Thin white stripes

# Draw the main stripes
# Black stripe
move_to(-FLAG_WIDTH / 2, FLAG_HEIGHT / 2)
draw_rectangle(FLAG_WIDTH, FLAG_HEIGHT / 3, "black")

# Red stripe
move_to(-FLAG_WIDTH / 2, FLAG_HEIGHT / 6)
draw_rectangle(FLAG_WIDTH, FLAG_HEIGHT / 3, "red")

# Green stripe
move_to(-FLAG_WIDTH / 2, -FLAG_HEIGHT / 6)
draw_rectangle(FLAG_WIDTH, FLAG_HEIGHT / 3, "green")

# Draw the white fimbriations over the red stripe's borders
move_to(-FLAG_WIDTH / 2, FLAG_HEIGHT / 6 + FIMBRIATION_HEIGHT)
draw_rectangle(FLAG_WIDTH, FIMBRIATION_HEIGHT, "white")
move_to(-FLAG_WIDTH / 2, -FLAG_HEIGHT / 6)
draw_rectangle(FLAG_WIDTH, FIMBRIATION_HEIGHT, "white")

# --- Draw the Central Emblem ---
# The order is important: draw the spears first, then the shield on top.

draw_spears()
draw_the_shield()

# Hide the turtle and finish
turtle.hideturtle()
turtle.done()