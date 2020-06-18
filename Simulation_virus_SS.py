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

    # infected or not (made to be random number but does not consider initially having 0 infected)
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

    # Making sure humans move initially
    if human.dy == 0:
        human.dy = 1
    if human.dx == 0:
        human.dx = 1

# Run Simulation
while True:
    wn.update()
    
    for human in humans:
        # Infecting humans
        """ Doesn't actually work.
            Changing properties of a turtle uses stamps?? (turtle.stamp())
            Code from stack overflow post about changing turtle colour here: https://stackoverflow.com/questions/40160808/python-turtle-color-change
            Can also be seen in file "color_change.py"

        X, Y = human.pos() # Gets the position of the first dot
        if human.color() == "red": # Check if infected
            for human in humans:
                x, y = human.pos() # Position of second dot
                Dx = x - X
                Dy = y - Y
                if human.color() == "blue": # If not infected
                    distance = math.sqrt(Dx^2 + Dy^2) # Pythagoras theorem
                    if distance < 50:
                        chance = random.randint(1, 2) # Infection chance
                        if chance == 1:
                            human.color("red") # Infected

        """

        # Moving Humans
        human.sety(human.ycor() + human.dy)
        human.setx(human.xcor() + human.dx)

        # humans randomly changing velocity
        # Direction
        confusion = random.randint(1, 500)
        if confusion == 69:
            human.dy *= -1
        if confusion == 420:
            human.dx *= -1
        if confusion == 31 or confusion == 400:
            human.dy *= -1
            human.dx *= -1

        # Magnitude (technically and direction)
        if confusion == 7:
            human.dy = random.randint(-2, 2)
            human.dx = random.randint(-2, 2)
        if confusion == 361:
            human.dy = random.randint(-2, 2)
        if confusion == 280:
            human.dx = random.randint(-2, 2)

        # Checking Humans stay in simulation (for fullscreen)
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