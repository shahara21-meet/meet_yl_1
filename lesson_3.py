import turtle
class Bird:
	def __init__ (self,name,color,speed):
		self.name=name
		self.color=color
		self.speed=speed
	def get_speed(self):
		print("the birds speed is "+self.speed)
	def race(self,competion_speed,competion_name):
		turtle1=turtle.clone()
		turtle.goto(0,50)
		for i in range(10):
			turtle.fd(self.speed)
			turtle1.fd(competion_speed)
		if turtle.xcor() > turtle1.xcor():
			print(self.name+" is the winner")
		elif turtle1.xcor() > turtle.xcor():
			print(competion_name+" is the winner")
		else:
			print("its a draw")

bird_1=Bird("lightning","blue",10)
bird_1.race(5,"slow lad")

