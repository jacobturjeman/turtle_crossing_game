from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.shape("turtle")
        self.goto(STARTING_POSITION)

    def move(self):
        """
        makes the turtle move by 10 pixels
        """
        self.forward(10)

    def new_game(self):
        """
        in case the player reached the edge of the screen and passed
        the cars, changes the turtles coordinates to the starting point
        to start again after gaining a point
        """
        self.goto(STARTING_POSITION)



