from turtle import Turtle

FONT = ("Courier", 24, "normal")


# creating a separate class for the scoreboard
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-180, 260)
        self.hideturtle()
        self.score = 0
        self.write(f"Score: {self.score}", font=("Courier", 24, "normal"))

    def gain(self):
        """
        when the player makes it to the other side of the screen
        he will gain a point which will be displayed on the scoreboard
        """
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", font=("Courier", 24, "normal"))

    def game_over(self):
        """
        a function to let the user know he lost and displays his final score
        """
        self.goto(-180, 0)
        self.write(f"Game Over\nYour final score is: {self.score}", font=("Courier", 24, "normal"))