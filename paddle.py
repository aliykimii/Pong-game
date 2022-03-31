
from turtle import Turtle

class Paddle(Turtle):
    '''create a paddle object and move it to a particular
     location specified'''
    def __init__(self,x_pos,y_pos):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.shape('square')
        self.color('blue')
        self.penup()
        self.turtlesize(0.5,5)
        self.setheading(90)
        self.goto(x_pos,y_pos)
        self.move_distance = 25

    def move_up(self):
        '''move the paddle up'''
        self.forward(self.move_distance)

    def move_down(self):
        '''move the paddle down'''
        self.backward(self.move_distance)


    
