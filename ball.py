from turtle import Turtle

class Ball(Turtle):
    '''creating a ball object from the ball class'''
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_increase = 3
        self.y_increase = 3

    def move(self):
           self.goto(self.xcor() + self.x_increase, self.ycor() + self.y_increase) 

    def change_y(self):
        self.y_increase *= -1

    def change_x(self):
        self.x_increase *= -1          

    def reset_ball(self):
        self.goto(0,0)   