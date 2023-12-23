from turtle import Screen
from spaceship import SpaceShip
import time
#from bullet import Bullet

screen = Screen()
screen.title("Space Impact")
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.tracer(0)

#bullet = Bullet()
ship = SpaceShip()
screen.listen()
screen.onkey(ship.left, "Left")
screen.onkey(ship.right, "Right")
screen.onkey(ship.bulletmove, "Up")
is_on = True
while is_on:
	screen.update()
	time.sleep(0)

	



screen.exitonclick()
