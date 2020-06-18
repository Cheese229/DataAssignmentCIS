import turtle
import random
import math

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Virus Spread Simulation")
wn.tracer(0)

# List of humans
humans = []

# Create Humans
for _ in range(30):
    humans.append(turtle.Turtle())

for human in humans:
    human.shape("circle")

    # infected or not
    i = random.randint(1, 20)
    if i == 1:
        color = "red"
    else:
        color = "blue"
    human.color(color)
    human.penup()
    human.speed(0)
    x = random.randint(-290, 290)
    y = random.randint(-290, 400)
    human.goto(x, y)
    human.dy = random.randint(-2, 2)
    human.dx = random.randint(-2, 2)

    # Making sure humans move
    if human.dy == 0:
        human.dy = 1
    if human.dx == 0:
        human.dx = 1

# Run Simulation
while True:
    wn.update()
    
    for human in humans:
        # Checking humans
        X, Y = human.pos()
        if human.color() == "red":
            for human in humans:
                x, y = human.pos()
                Dx = x - X
                Dy = y - Y
                if human.color() == "blue":
                    distance = math.sqrt(Dx^2 + Dy^2)
                    if distance < 50:
                        chance = random.randint(1, 2)
                        if chance == 1:
                            human.color("red")

        # Moving Humans
        human.sety(human.ycor() + human.dy)
        human.setx(human.xcor() + human.dx)

        # humans randomly changing velocity
        confusion = random.randint(1, 500)
        if confusion == 69:
            human.dy *= -1
        if confusion == 420:
            human.dx *= -1
        if confusion == 31 or confusion == 400:
            human.dy *= -1
            human.dx *= -1

        if confusion == 7:
            human.dy = random.randint(-2, 2)
            human.dx = random.randint(-2, 2)
        if confusion == 361:
            human.dy = random.randint(-2, 2)
        if confusion == 280:
            human.dx = random.randint(-2, 2)

        # Checking Humans stay in simulation
        if human.xcor() > 700:
            human.setx(700)
            human.dx *= -1
            
        if human.xcor() < -700:
            human.setx(-700)
            human.dx *= -1

        if human.ycor() < -400:
            human.sety(-400)
            human.dy *= -1

        if human.ycor() > 400:
            human.sety(400)
            human.dy *= -1

        

wn.mainloop()