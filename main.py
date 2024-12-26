import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
CarManager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun= player.forward_move, key= "Up")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    CarManager.create_cars()
    CarManager.move_cars()
#     detect collison with cars
    for car in CarManager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() == 280:
        player.goto(0, -280)
        CarManager.level_up()
        scoreboard.increase_level()

screen.exitonclick()