from turtle import *
import turtle

# assigning window as turtle screen
window = turtle.Screen()

# Title Bar (Naming)
window.title("Make Square using Turtle")

# Assigning arrow as turtle
arrow = turtle.Turtle()

def square():
    for i in range(5):
        arrow.forward(90)   #Distance 50px
        arrow.right(90)     #angle 90 degree

#square()

def star():
    arrow.right(75) #degree
    arrow.forward(100) #move 100px forward
    for i in range(4):
        arrow.right(144)
        arrow.forward(100)
#star()


def polygon():
    number_of_sides = 6 #Number of sides
    size_length = 70 #Length of Sides
    angle = (360.0/ number_of_sides) # finding angle

    for i in range(number_of_sides):
        arrow.forward(size_length)
        arrow.right(angle)
polygon()

turtle.done()