"""
    Learning the basics of python's turtle module
    Simple bouncing ball simulation
"""

import turtle
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Bouncing Ball Simulation")
wn.tracer(0)

balls = []
colors = ["red", "blue", "green", "yellow", "orange", "white", "purple", "pink"]
shapes = ["circle", "triangle", "square"]

# Creates balls of ammount
for _ in range(20):
    balls.append(turtle.Turtle())

# Creates starting features of each ball
for ball in balls:
    ball.shape(random.choice(shapes))
    ball.color(random.choice(colors))
    ball.penup()
    ball.speed(0)
    x = random.randint(-290, 290)
    y = random.randint(200, 400)
    ball.goto(x, y)
    ball.dy = -1
    ball.dx = random.randint(-3, 3)
    ball.da = random.randint(-5, 5)

g = 0.05

# Updating animation and changing depending on senario
while True:
    wn.update()

    for ball in balls:
        ball.rt(ball.da)
        ball.dy -= g
        ball.sety(ball.ycor() + ball.dy)

        ball.setx(ball.xcor() + ball.dx)
        
        # bounces off right wall
        if ball.xcor() > 300:
            ball.setx(300)
            ball.dx *= -1
            ball.da *= -1
        
        # bounces off left wall
        if ball.xcor() < -300:
            ball.setx(-300)
            ball.dx *= -1
            ball.da *= -1
        
        # bounces off floor
        if ball.ycor() < -300:
            ball.sety(-300)
            ball.dy *= -1
            ball.da *= -1


wn.mainloop()