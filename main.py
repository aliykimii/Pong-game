from turtle import Turtle ,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from round import Round

#creating the screen
my_screen = Screen()

my_screen.tracer(0)
my_screen.setup(width = 800, height = 600)
user_round = my_screen.textinput("Ping Pong Game","How many round you want to play?")
int_round = int(user_round)
my_screen.bgcolor("black")

#creating the paddle and moving the paddles
l_paddle = Paddle(-390,0)
r_paddle = Paddle(380,0)
my_screen.onkey(r_paddle.move_up, "Up")
my_screen.onkey(r_paddle.move_down, "Down")
my_screen.onkey(l_paddle.move_up, "w")
my_screen.onkey(l_paddle.move_down, "s")
my_screen.listen()




#creating a scoreboard and round display
round = Round(-90,230)
scoreboard = Scoreboard(-350,230)
highscore = Scoreboard(280,230)
my_screen.tracer(1)
endgame = 0
#creating ball
ball = Ball()
game_on = True
while game_on == True:
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.change_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 370:
        ball.change_x()

    if ball.distance(l_paddle) < 50 and ball.xcor() > -370:
        ball.change_x()  

    if ball.xcor() > 400:
        scoreboard.add_left()
        highscore.left_highscores()
        round.add_round()
        endgame += 1
        my_screen.tracer(0)
        ball.reset_ball()    
        my_screen.tracer(1)
    
    if ball.xcor() < -400:
        scoreboard.add_right()
        highscore.right_highscores()
        round.add_round()
        endgame += 1
        my_screen.tracer(0)
        ball.reset_ball()
        my_screen.tracer(1)

    if endgame == int_round:
        game_on = False
#ensure screen doesnt go out
my_screen.mainloop()