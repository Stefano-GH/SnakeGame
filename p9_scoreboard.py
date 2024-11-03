from turtle import Turtle

alignment = "center"
font = ("Arial", 22, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("p9_data.txt") as data:
            self.highscore = int(data.read())
            data.close()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
    
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.highscore}", align=alignment, font=font)
    
    
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("p9_data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
                data.close()
        self.score = 0
        self.update_scoreboard()
    
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=alignment, font=font)
    
    
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()