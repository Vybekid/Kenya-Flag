import turtle

def move_to(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def draw_rectangle(width, height, color):
    turtle.color(color, color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

turtle.setup(width=800, height=500)
turtle.speed(3)
turtle.bgcolor("#f0f0f0")
turtle.title("Flag of Kenya - Stripes")

FLAG_WIDTH = 600
FLAG_HEIGHT = 400
TOTAL_PARTS = 20
MAIN_STRIPE_HEIGHT = FLAG_HEIGHT * 6 / TOTAL_PARTS
FIMBRIATION_HEIGHT = FLAG_HEIGHT * 1 / TOTAL_PARTS

y_pos = FLAG_HEIGHT / 2

move_to(-FLAG_WIDTH / 2, y_pos)
draw_rectangle(FLAG_WIDTH, MAIN_STRIPE_HEIGHT, "black")
y_pos -= MAIN_STRIPE_HEIGHT

move_to(-FLAG_WIDTH / 2, y_pos)
draw_rectangle(FLAG_WIDTH, FIMBRIATION_HEIGHT, "white")
y_pos -= FIMBRIATION_HEIGHT

move_to(-FLAG_WIDTH / 2, y_pos)
draw_rectangle(FLAG_WIDTH, MAIN_STRIPE_HEIGHT, "red")
y_pos -= MAIN_STRIPE_HEIGHT

move_to(-FLAG_WIDTH / 2, y_pos)
draw_rectangle(FLAG_WIDTH, FIMBRIATION_HEIGHT, "white")
y_pos -= FIMBRIATION_HEIGHT

move_to(-FLAG_WIDTH / 2, y_pos)
draw_rectangle(FLAG_WIDTH, MAIN_STRIPE_HEIGHT, "green")

turtle.hideturtle()
turtle.done()