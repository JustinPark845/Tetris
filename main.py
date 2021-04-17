### To run code copy command into terminal: sudo python3 /Users/justinpark/Desktop/Code/tetris/main.py ###

from turtle import Turtle, Screen
from layout import Layout
from block_bot import Block_Bot
from countdown import Countdown

#initialize screen
screen = Screen()
screen.setup(width=600, height=1800)
screen.bgcolor("black")
screen.title("Tetris")
screen.tracer(0)

layout = Layout()
countdown = Countdown()
block_bot = Block_Bot()

screen.update()
# countdown.countdown()
while not block_bot.game_over():
    block_bot.blocks.goto(-15,285)
    block_bot.game_progressor()
    screen.update()

layout.game_over()
screen.exitonclick()


#current bugs
#line dropper
#   hold and space f ups the recording of the color lists
#   afte a while, the perm coord stuff gets messed up


#z and s fix
#hold spaz fix
#score
#comments