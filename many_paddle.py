import turtle as tt
import random

class CreateTurtle(tt.Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.penup()
        self.shape('Gif/invader.gif')
        self.shapesize(stretch_wid=1.5, stretch_len=3)
        self.color('white')
        self.setposition(x=x_cor, y=y_cor)
 
 
class ManyTurtle:
    def __init__(self):
        self.y_start = 200
        self.y_end = 350
        self.enemies = []
        self.enemyspeed = 10
        self.create_all_lanes()
 
    def create_lane(self, y_cor):
        for i in range(-300, 300, 63):
            brick = CreateTurtle(i, y_cor)
            self.enemies.append(brick)
 
    def create_all_lanes(self):
        for i in range(self.y_start, self.y_end, 32):
            self.create_lane(i)