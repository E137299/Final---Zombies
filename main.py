from turtle import *
from random import randint, choice

#### CLASS AND FUNCTION DEFINITIONS #####
def playing_area():
	t = Turtle()
	t.speed(0)
	t.ht()
	t.pu()
	t.goto(-250,250)
	t.color("light blue")
	t.pd()
	t.begin_fill()
	for i in range(4):
		t.forward(500)
		t.right(90)
	t.end_fill()

'''
Player() Class

Constructor( def __init__(self)):
- player should be shaped like a turtle.
- will take in the x and y coordinates for where the player will initially appear.
- will take in a color for the player
- will take in keys to turn left, turn right and shoot bullets.
- player will have an attribute that is a list that stores bullets

move(self):
- moves object forward five pixels
'''
class Player(Turtle):
	pass

#### DRIVER CODE ####
screen = Screen()
screen.bgcolor("black")

playing_area()


screen.mainloop()
