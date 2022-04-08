import time
from turtle import Screen, Turtle


# Screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# keystrokes
screen.listen()
screen.update()


def move_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)
def move_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)

screen.onkeypress(key="Up", fun=move_up)
screen.onkeypress(key="Down", fun=move_down)

# shape the paddle
paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.penup()
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.goto(x=350, y=0)

game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()