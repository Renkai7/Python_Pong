import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

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
# Scoreboard
scoreboard = Scoreboard()

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
    time.sleep(ball.move_speed)
    # sets angle of ball and moves forward
    ball.move()
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when right paddle misses ball
    if ball.xcor() > 380:
        ball.ball_reset()
        scoreboard.l_point()

    # Detect when left paddles misses ball
    if ball.xcor() < -380:
        ball.ball_reset()
        scoreboard.r_point()

screen.exitonclick()
