from turtle import Turtle, Screen
from random import randrange, choice
from collections import namedtuple
from math import ceil

GRID = 15  # GRID by GRID of squares
SIZE = 30  # each square is SIZE by SIZE

INCREASE = 1.5  # how much to lighten the square's color
WHITE = [255, 255, 255]  # color at which we stop changing square
DELAY = 100  # time between calls to change() in milliseconds
DARK = 32 # range (ceil(INCREASE) .. DARK - 1) of dark colors

def change():
    block = choice(blocks)
    blocks.remove(block)

    color = [min(int(primary * INCREASE), WHITE[i]) for i, primary in enumerate(block.color)]  # lighten color

    turtle.color(color)
    turtle.setposition(block.position)
    turtle.clearstamp(block.stamp)

    stamp = turtle.stamp()

    if color != WHITE:
        blocks.append(Block(block.position, color, stamp))  # not white yet so keep changing this block

    if blocks:  # stop all changes if/when all blocks turn white
        screen.ontimer(change, DELAY)

HALF_SIZE = SIZE // 2

screen = Screen()
screen.colormode(WHITE[0])
screen.register_shape("block", ((HALF_SIZE, -HALF_SIZE), (HALF_SIZE, HALF_SIZE), (-HALF_SIZE, HALF_SIZE), (-HALF_SIZE, -HALF_SIZE)))
screen.tracer(GRID ** 2)  # ala @PyNuts

turtle = Turtle(shape="block", visible=False)
turtle.speed("fastest")
turtle.up()

Block = namedtuple('Block', ['position', 'color', 'stamp'])

blocks = list()

HALF_GRID = GRID // 2

for x in range(-HALF_GRID, HALF_GRID):
    for y in range(-HALF_GRID, HALF_GRID):
        turtle.goto(x * SIZE, y * SIZE)
        color = [randrange(ceil(INCREASE), DARK) for primary in WHITE]
        turtle.color(color)
        blocks.append(Block(turtle.position(), color, turtle.stamp()))

screen.ontimer(change, DELAY)

screen.exitonclick()