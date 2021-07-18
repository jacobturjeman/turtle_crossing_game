### The objective is to create the game Crossing Turtle using 'turtle' library
import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def move_cars(car_list):
    """
    make the cars move by accessing each created car that's being
    appended to the list and activating move function on them
    """
    num = 0
    for i in car_list:
        car_list[num].move()
        num += 1


def detect_collision(car_list, tsav):
    """
    check for a collision between the turtle and a car
    """
    num = 0
    for i in car_list:
        if tsav.distance(car_list[num]) < 20:
            score.game_over()
            return False
        num += 1
    return True


# set the level of the game in the form of a condition,
# it actually changes the amount of car objects being created
def level():
    if random.randint(0, 9) > 7:
        return True
    else:
        return False


# creating a list which will include all of the 'car' objects in order to
cars = []
# setting up the screen, score and the actual turtle which we will be in control of
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
score = Scoreboard()
player = Player()
# setting the "Up" key to make the turtle to move upwards
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    # create the 'cars'
    if level():
        car = CarManager()
        cars.append(car)
    move_cars(cars)
    # end the game if there is a collision
    game_is_on = detect_collision(cars, player)
    # keep track of score
    if player.ycor() > 300:
        score.gain()
        player.new_game()
    screen.update()
screen.exitonclick()
