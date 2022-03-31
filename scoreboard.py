from turtle import Turtle

class Scoreboard(Turtle):
    '''creating the scoreboard for the game'''
    def __init__(self,x_pos,y_pos):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(x_pos,y_pos)
        self.l_player = 0
        self.r_player = 0
        left_file = 'left_player.txt'
        with open(left_file) as left_file:
            self.left_highscore = int(left_file.read())
        right_file = 'right_player.txt'
        with open(right_file) as right_file:
            self.right_highscore = int(right_file.read())  

        self.write(f"{self.l_player} : {self.r_player}", font = ('segoe UI',40,'normal'))

    def add_right(self):
        '''add 1 to the right player score''' 
        self.clear() 
        self.r_player += 1  
        self.write(f"{self.l_player} : {self.r_player}", font = ('segoe UI',40,'normal'))

    
    def add_left(self):
        '''add 1 to the left player score'''
        self.clear()  
        self.l_player += 1      
        self.write(f"{self.l_player} : {self.r_player}", font = ('segoe UI',40,'normal'))

        


    def right_highscores(self):

        if self.r_player > self.right_highscore:
            self.right_highscore = self.r_player
            with open('right_player.txt', mode = 'w') as right_data:
                right_data.write(f"{self.right_highscore}")        
        self.clear()
        self.write(f"{self.left_highscore} : {self.right_highscore}", font = ('segoe UI',40,'normal'))

    def left_highscores(self):

        if self.l_player > self.left_highscore:
            self.left_highscore = self.l_player
            with open('left_player.txt', mode = 'w') as left_data:
                left_data.write(f"{self.left_highscore}")

        self.clear()
        self.write(f"{self.left_highscore} : {self.right_highscore}", font = ('segoe UI',40,'normal'))    