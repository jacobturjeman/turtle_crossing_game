from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


# the settings of each car as it being created
class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(COLORS[random.randint(0, 5)])
        y = random.randint(-250, 250)
        x = 280
        self.goto(x, y)
        self.setheading(180)

    def move(self):
        """
        getting the object's current position and moves it
        along the x axis by changing its x coordinate
        """
        x = (self.xcor() - STARTING_MOVE_DISTANCE)
        y = (self.ycor())
        self.goto(x, y)

    # working on ways to improve the level mechanism
    # def new_level(self):
    #     self.speed += MOVE_INCREMENT


