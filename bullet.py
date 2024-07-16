from turtle import Turtle

class Bullet(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('triangle')
        self.speed(0)
        self.shapesize(0.5,0.5)
        self.color('yellow')
        self.penup()
        self.hideturtle()
        self.setheading(90)
        self.bulletspeed = 70
        self.bulletstate = "ready"

    def fire_bullet(self, x, y):
        if self.bulletstate == 'ready':
            self.bulletstate = "fire"
            y = y + 10
            self.setposition(x, y)
            self.showturtle()