from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        #self.shape("")
        self.penup()
        self.goto(0, 260)
        self.clear()
        self.score = 0
        #self.highscore = 0

        with open("scorelog.txt") as file:
            self.highscore = file.read()
            if self.highscore == '':
                self.highscore = "0"


        self.write(f"Score: {self.score}      Highscore: {self.highscore}", False, align="Center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > int(self.highscore):
            self.highscore = self.score
            with open("scorelog.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.clear()
        self.score = 0
        self.write(f"Score: {self.score}      Highscore: {self.highscore}", False, align="Center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}      Highscore: {self.highscore}", False, align="Center", font=("Arial", 24, "normal"))
