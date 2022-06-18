import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800,height=600)
screen.title("PING PONG")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    # Dectect collision with paddle
    if ball.distance(r_paddle) < 100 and ball.xcor() > 320 or ball.distance(l_paddle) < 100 and ball.xcor() < -320:
        ball.bounce_x() 
    
    # Dectect R paddle miss
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()

    # Detect L paddle miss
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()

           
screen.exitonclick()