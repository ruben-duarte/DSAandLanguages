from processing_py import *
import random
app = App(400,400)

class Star:
    
    x = random(0, app.width)
    y = random(0, app.height)
    z = random(0, app.width)

    def update(self):
        pass

    def show(self):
        app.fill(255)
        app.noStroke()
        app.ellipse(self.x,self.y,8,8)

#link  https://pypi.org/project/processing-py/

stars = [i*0 for i in range(100)]
for item in range(len(stars)):
        stars[item] = Star()

def draw():
    app.background(0)
    for item in range(len(stars)):
       stars[item].update()
       stars[item].show()
