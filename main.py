import turtle as tt
from paddle import Paddle
from score import Score
from many_paddle import ManyTurtle
from bullet import Bullet
import math

wn = tt.Screen()
wn.bgcolor('black')
wn.title('Space invaders')
wn.setup(width=800, height=800)

tt.register_shape("Gif/invader.gif")
tt.register_shape("Gif/player.gif")

paddle = Paddle()
score = Score()
enemies = ManyTurtle()
bullet = Bullet()

def bullet_f():
    bullet.fire_bullet(paddle.xcor(), paddle.ycor())

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 20:
        return True
    else:
        return False

tt.listen()
tt.onkey(paddle.left, 'Left')
tt.onkey(paddle.right, 'Right')
tt.onkey(bullet_f, 'space')

while True:
    for enemy in enemies.enemies:
        x = enemy.xcor()
        x -= enemies.enemyspeed
        enemy.setx(x)

        if enemy.xcor() > 380:
            enemies.enemyspeed *= -1

        if enemy.xcor() < -380:
            enemies.enemyspeed *= -1

        if isCollision(bullet, enemy):
            bullet.hideturtle()
            bullet.bulletstate = 'ready'
            bullet.setposition(0,-440)
            enemy.hideturtle()
            score.score += 10
            score.scorestring = "Score: %s" %score.score
            score.clear()
            score.write(score.scorestring, False, align="left", font=("Arial",14,"normal"))

        if isCollision(paddle, enemy):
            paddle.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break

    if bullet.bulletstate == 'fire':
        y = bullet.ycor()
        y += bullet.bulletspeed
        bullet.sety(y)

    if bullet.ycor() > 385:
        bullet.hideturtle()
        bullet.bulletstate = 'ready'