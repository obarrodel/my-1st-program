from turtle import Turtle

STEP = 10

class SpaceShip(Turtle):
	def __init__(self):
		super().__init__()


		self.shape("turtle")
		self.color("white")
		self.penup()
		self.goto(0, -250)
		self.setheading(90)

		self.bullet = Turtle()
		self.bullet.shape("circle")
		self.bullet.hideturtle()
		self.bullet.penup()
		self.bullet.setheading(90)
		self.bullet.color("red")


	def left(self):
		self.goto(self.xcor() - STEP, self.ycor())

	def right(self):
		self.goto(self.xcor() + STEP, self.ycor())


	def bulletmove(self):
		self.bullet.showturtle()
		for _ in range(28):
			self.bullet.forward(STEP)






