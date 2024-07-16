from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.color('white')
        self.penup()
        self.setposition(-390,380)
        self.score = 0
        self.scorestring = "Score: %s" %self.score
        self.write(self.scorestring, False, align="left", font=("Arial",14,"normal"))
        self.hideturtle()