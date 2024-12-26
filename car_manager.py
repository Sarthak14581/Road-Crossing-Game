COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
import random
from turtle import Turtle
X = 600


class CarManager():

    def __init__(self):
         self.all_cars = []
         self.carspeed = STARTING_MOVE_DISTANCE

    def create_cars(self):
         random_chance = random.randint(0,6)
         if random_chance == 3:
             new_car = Turtle("square")
             new_car.shapesize(stretch_wid=1, stretch_len=2)
             new_car.penup()
             new_car.color(random.choice(COLORS))
             random_y = random.randint(-250, 250)
             new_car.goto(300, random_y)
             self.all_cars.append(new_car)
             new_car.setheading(180)

    def move_cars(self):
         for car in self.all_cars:
              car.forward(self.carspeed)


    def level_up(self):
        self.carspeed += MOVE_INCREMENT


