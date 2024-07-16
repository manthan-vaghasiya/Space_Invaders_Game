from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('Gif/player.gif')
        self.color('white')
        self.penup()
        self.setposition(0, -350)
        self.setheading(90)
        self.playerspeed = 15

    def left(self):
        new_x = self.xcor()
        new_x -= self.playerspeed
        if new_x < -380:
            new_x = -380
        return self.setx(new_x)

    def right(self):
        new_x = self.xcor()
        new_x += self.playerspeed
        if new_x > 380:
            new_x = 380
        return self.setx(new_x)