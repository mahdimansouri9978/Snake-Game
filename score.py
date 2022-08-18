from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        with open("score.txt") as score:
            self.highscore = int(score.read())
        self.goto(0, 260)
        self.speed("fastest")
        self.color("white")
        self.write(arg=f"score: {self.score} High score: {self.highscore}", align="center", font=("courier", 24, "normal"))
    def increes(self):
        self.score += 1
        self.update()
    def update(self):
        self.clear()
        self.score += 1
        self.write(arg=f"score: {self.score} High score: {self.highscore}", align="center",
                   font=("courier", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over !!", align="center", font=("courier", 24, "normal"))
    def game_repeat(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("score.txt", mode="w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.clear()
        self.write(arg=f"score: {self.score} High score: {self.highscore}", align="center",
                   font=("courier", 24, "normal"))

