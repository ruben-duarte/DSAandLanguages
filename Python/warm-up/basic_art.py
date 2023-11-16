from turtle import *
import random

setup(500, 500)
bgcolor("#70A9A1")

def tiling(x,y,size,level):
    #base case
    if level == 0:

        if random.random() < 0.5:
            #vertical line
            penup()
            goto(x,y - size)
            pendown()
            goto(x,y + size)
        else:
            #horizontal line
            penup()
            goto(x - size,y)
            pendown()
            goto(x + size,y)
    else:
        size /= 2
        level -= 1
        tiling(x - size,y + size,size,level)
        tiling(x + size ,y + size,size,level)
        tiling(x - size,y - size,size,level)
        tiling(x + size,y - size,size,level)


width(3)
tiling(0,0,200,4)
exitonclick()


