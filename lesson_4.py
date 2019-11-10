import turtle
from turtle import Turtle
class ball(Turtle):
	def __init__(self,r,color,dx,dy,status):
		Turtle.__init__(self)
		self.r=r
		self.color=color
		self.dx=dx
		self.dy=dy
		self.size=r/10
		self.status=status
		turtle.penup()

	def move(self,screen_l,screen_w):
		c_x_pos=turtle.xcor()
		n_x_pos=c_x_pos+self.dx
		c_y_pos=turtle.ycor()
		n_y_pos=c_y_pos+self.dy

		r_size_ball=n_x_pos+self.r
		l_size_ball=-n_x_pos-self.r
		u_size_ball=n_y_pos+self.r
		d_size_ball=-n_y_pos-self.r
		turtle.goto(n_x_pos,n_y_pos)
		
		while self.status==True:
			if r_size_ball >= screen_w:
				turtle.goto(turtle.xcor()-1,turtle.ycor())
			if l_size_ball <=-screen_w:
				turtle.goto(turtle.xcor()+1,turtle.ycor())
			if u_size_ball >= screen_l:
				turtle.goto(turtle.xcor(),turtle.ycor()-1)
			if d_size_ball <=-screen_l:
				turtle.goto(turtle.xcor(),turtle.ycor()+1)



screen_w=turtle.getcanvas().winfo_width()/2
screen_l=turtle.getcanvas().winfo_height()/2

ball1=ball(5,"Blue",10,5,True)
while True:

	ball1.move(screen_l,screen_w)


