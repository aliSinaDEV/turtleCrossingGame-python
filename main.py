import turtle
from turtle import Turtle, Screen
from carmanager import CarManager
from player import Player
from scoreboard import Scoreboard

import time

my_screen = Screen()
my_screen.tracer(0)

my_screen.setup(width=600, height=600)
my_screen.bgcolor("white")

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

my_screen.listen()

my_screen.onkey(fun=player.move, key="Up")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    my_screen.update()
    new_car = car_manager.create_car()
    car_manager.move_cars()

    #Detecct collision with car
    for cars in car_manager.all_cars:
        if player.distance(cars) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.add_score()


my_screen.exitonclick()