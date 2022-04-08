import time
from turtle import Screen, Turtle


# Screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
# screen.tracer(False)

# keystrokes
screen.listen()
screen.update()
time.sleep(0.8)

def move_up():
    # paddle.setheading(90)
    paddle.forward(20)
def move_down():
    # paddle.setheading(270)
    paddle.forward(-20)

screen.onkeypress(key="Up", fun=move_up)
screen.onkeypress(key="Down", fun=move_down)

# shape the paddle
paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.penup()
paddle.setheading(90)
paddle.shapesize(stretch_wid=2, stretch_len=8)
paddle.setposition(x=350, y=0)




screen.exitonclick()