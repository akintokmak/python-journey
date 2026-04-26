import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()

screen.title("PONG-Game")
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.tracer(0)

r_paddle = Paddle(position=(350,0))
l_paddle = Paddle(position=(-350,0))

ball = Ball()
score_board = Scoreboard()
screen.listen()
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")
screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key='s')

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #Detect collision with wall
    if  ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    #Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score_board.l_point()
    #Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score_board.r_point()







screen.exitonclick()