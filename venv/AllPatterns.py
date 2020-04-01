import turtle

wn=turtle.Screen()
wn.setup(width=700,height=700)
wn.title("Patterns")
wn.bgcolor("black")

turtle.speed(0)
turtle.color("cyan")

colors = [
        # reddish colors
        (1.00, 0.00, 0.00), (1.00, 0.03, 0.00), (1.00, 0.05, 0.00), (1.00, 0.07, 0.00), (1.00, 0.10, 0.00),
        (1.00, 0.12, 0.00), (1.00, 0.15, 0.00), (1.00, 0.17, 0.00), (1.00, 0.20, 0.00), (1.00, 0.23, 0.00),
        (1.00, 0.25, 0.00), (1.00, 0.28, 0.00), (1.00, 0.30, 0.00), (1.00, 0.33, 0.00), (1.00, 0.35, 0.00),
        (1.00, 0.38, 0.00), (1.00, 0.40, 0.00), (1.00, 0.42, 0.00), (1.00, 0.45, 0.00), (1.00, 0.47, 0.00),
        # orangey colors
        (1.00, 0.50, 0.00), (1.00, 0.53, 0.00), (1.00, 0.55, 0.00), (1.00, 0.57, 0.00), (1.00, 0.60, 0.00),
        (1.00, 0.62, 0.00), (1.00, 0.65, 0.00), (1.00, 0.68, 0.00), (1.00, 0.70, 0.00), (1.00, 0.72, 0.00),
        (1.00, 0.75, 0.00), (1.00, 0.78, 0.00), (1.00, 0.80, 0.00), (1.00, 0.82, 0.00), (1.00, 0.85, 0.00),
        (1.00, 0.88, 0.00), (1.00, 0.90, 0.00), (1.00, 0.93, 0.00), (1.00, 0.95, 0.00), (1.00, 0.97, 0.00),
        # yellowy colors
        (1.00, 1.00, 0.00), (0.95, 1.00, 0.00), (0.90, 1.00, 0.00), (0.85, 1.00, 0.00), (0.80, 1.00, 0.00),
        (0.75, 1.00, 0.00), (0.70, 1.00, 0.00), (0.65, 1.00, 0.00), (0.60, 1.00, 0.00), (0.55, 1.00, 0.00),
        (0.50, 1.00, 0.00), (0.45, 1.00, 0.00), (0.40, 1.00, 0.00), (0.35, 1.00, 0.00), (0.30, 1.00, 0.00),
        (0.25, 1.00, 0.00), (0.20, 1.00, 0.00), (0.15, 1.00, 0.00), (0.10, 1.00, 0.00), (0.05, 1.00, 0.00),
        # greenish colors
        (0.00, 1.00, 0.00), (0.00, 0.95, 0.05), (0.00, 0.90, 0.10), (0.00, 0.85, 0.15), (0.00, 0.80, 0.20),
        (0.00, 0.75, 0.25), (0.00, 0.70, 0.30), (0.00, 0.65, 0.35), (0.00, 0.60, 0.40), (0.00, 0.55, 0.45),
        (0.00, 0.50, 0.50), (0.00, 0.45, 0.55), (0.00, 0.40, 0.60), (0.00, 0.35, 0.65), (0.00, 0.30, 0.70),
        (0.00, 0.25, 0.75), (0.00, 0.20, 0.80), (0.00, 0.15, 0.85), (0.00, 0.10, 0.90), (0.00, 0.05, 0.95),
        # blueish colors
        (0.00, 0.00, 1.00), (0.05, 0.00, 1.00), (0.10, 0.00, 1.00), (0.15, 0.00, 1.00), (0.20, 0.00, 1.00),
        (0.25, 0.00, 1.00), (0.30, 0.00, 1.00), (0.35, 0.00, 1.00), (0.40, 0.00, 1.00), (0.45, 0.00, 1.00),
        (0.50, 0.00, 1.00), (0.55, 0.00, 1.00), (0.60, 0.00, 1.00), (0.65, 0.00, 1.00), (0.70, 0.00, 1.00),
        (0.75, 0.00, 1.00), (0.80, 0.00, 1.00), (0.85, 0.00, 1.00), (0.90, 0.00, 1.00), (0.95, 0.00, 1.00)
    ]

def pattern1():
    for i in range(100):
        turtle.circle(5 * i)
        turtle.circle(-5 * i)
        turtle.left(i)


def pattern2():
    for i in range(100000000):
        turtle.circle(10 * i)
        turtle.circle(-10 * i)

def pattern3():
    turtle.colormode(255)
    turtle.speed(0)

    for i in range(100):
        turtle.circle(5 * i)
        turtle.color(1 * i, i + i - 2 * i, i + i)
        turtle.circle(-5 * i)


def pattern4():
    for i in range(100000):
        turtle.circle(i)
        turtle.left(i)



def pattern5():
    side = 4

    def shape(size, sides):
        for i in range(sides):
            turtle.forward(size)
            turtle.left(90)

    for i in range(100000):
        shape(i * 5, side)
        turtle.left(i)

def pattern6():
    sides = 4

    def shape(size, sides):
        for i in range(sides):
            turtle.forward(size)
            turtle.left(360 / sides)

    for i in range(100000):
        shape(i, sides)
        turtle.left(i)


def pattern7():
    sides = 4

    # Try different sides, you will be surprised...

    def shape(size, sides):
        for i in range(sides):
            turtle.forward(size)
            turtle.left(360 / sides)

    for i in range(100000):
        shape(i, sides)
        turtle.left(360 / sides)  # keep this line same

def pattern7():
    sides = 4

    # Try different sides, you will be surprised...

    def shape(size, sides):
        for i in range(sides):
            turtle.forward(size)
            turtle.left(360 / sides)

    for i in range(100000):
        shape(i, sides)
        turtle.left(360 / sides)  # keep this line same for

def pattern8():
    sides = 4

    def shape(size, sides):
        for i in range(sides):
            turtle.forward(size)
            turtle.left(360 / sides)


    for i in range(255):
        shape(i, sides)
        turtle.left(sides)


def pattern9():
    sides = 4

    def shape(size, sides):
        for i in range(sides):
            turtle.forward(size)
            turtle.left(360 / sides)

    for i in range(100000):
        shape(i, sides)
        turtle.left(180)


def pattern10():
    sides = 4

    def square(sides):
        for i in range(sides):
            turtle.forward(200)
            turtle.left(360 / sides)


    for i in range(100):
        square(sides)
        turtle.left(180)
        for j in range(1):
            turtle.left(5)
            square(sides)
            turtle.left(180)

def pattern11():
    c=0
    x=0

    while x < 1000:
        idx = int(c)
        color = colors[idx]
        turtle.color(color)
        turtle.forward(x)
        turtle.right(98)
        x = x + 1
        c = c + 0.1


def pattern12():
    index=0
    id=0

    sides=4

    def squares(sides,color):
        for i in range(sides):
            turtle.color(color)
            turtle.forward(200)
            turtle.left(360/sides)

    while(index<=100):
        id = int(index)
        color=colors[id]
        squares(sides,color)
        index += 0.5
        turtle.left(180)
        for j in range(1):
            turtle.left(5)
            squares(sides,color)
            turtle.left(180)








#run a pattern

pattern11()

#exit on click
turtle.done