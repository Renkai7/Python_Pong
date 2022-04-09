import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball

# Screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
# Ball
ball = Ball()

# keystrokes
screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    # control speed of ball
    time.sleep(0.1)
    # sets angle of ball and moves forward
    ball.move()

    # Detect collision with wall
    if ball.xcor() > 480 or ball.xcor() < -480:
        game_is_on = False
    elif ball.ycor() > 280 or ball.ycor() < -280:
        # need to bounce
        ball.bounce()

screen.exitonclick()