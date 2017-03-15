import turtle


def draw_square(some_turtle):
	for i in range(1, 5):
		some_turtle.forward(200)
		some_turtle.right(90)

def draw_rhombus(some_turtle):
	for i in range(1, 3):
		some_turtle.forward(100)
		some_turtle.right(45)
		some_turtle.forward(100)
		some_turtle.right(135)
			
def draw_circle(some_turtle):
	some_turtle.goto(0, -100)
	some_turtle.circle(100)
	some_turtle.right(90)
	some_turtle.forward(200)	

def draw_art():
	window = turtle.Screen()
	window.bgcolor("dark grey")
	# use class Turtle
	# create turtle to draw rhombus
	brad = turtle.Turtle()
	brad.shape("circle")
	brad.color("pink")
	brad.speed(15)
	for i in range (1, 37):
		draw_rhombus(brad)
		brad.right(10)
	# create turtle to draw circle
	angie = turtle.Turtle()
	angie.shape("circle")
	angie.color("light blue")
	angie.speed(10)
	draw_circle(angie)

	window.exitonclick()

draw_art()