from turtle import Turtle, Screen
import time
ALIGN = "center"
FONT = ("Impact", 50, "normal")

class Countdown():
    def __init__(self):
        self.screen = Screen()

    def countdown(self):
        countdown_bot = Turtle()
        countdown_bot.hideturtle()
        countdown_bot.penup()
        countdown_bot.goto(0,0)
        countdown_bot.pencolor("white")
        count = 3
        while count != 0:
            countdown_bot.write(f"{count}", align = ALIGN, font = FONT)
            self.screen.update()
            time.sleep(1)
            countdown_bot.clear()
            count = count - 1
            

