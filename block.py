from turtle import Turtle

class Block(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(1.4, 1.4, 1.4)
        self.shape("square")
        self.penup()
        self.speed(10)
        self.hideturtle()
