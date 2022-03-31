from turtle import Turtle

class  Round(Turtle):
    def __init__(self,xpos,ypos):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(xpos,ypos)
        self.num_round = 1
        self.write(f"Round {self.num_round}", font = ('segoe UI',40,'normal'))

    def add_round(self):
        self.clear()
        self.num_round += 1
        self.write(f"Round {self.num_round}", font = ('segoe UI',40,'normal'))    