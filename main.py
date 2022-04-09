import time
from turtle import Screen, Turtle
from paddle import Paddle

# Screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# keystrokes
screen.listen()

screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")

# Ball
ball = Turtle()
ball.shape("circle")
ball.color("blue")
ball.penup()


game_is_on = True
while game_is_on:
    screen.update()
    # control speed of ball
    time.sleep(0.1)
    # sets angle of ball and moves foward
    ball.setheading(20)
    ball.forward(20)

screen.exitonclick()