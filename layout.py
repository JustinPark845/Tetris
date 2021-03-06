from turtle import Turtle
ALIGN = "center"
FONT = ("Impact", 50, "normal")

class Layout(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.draw_title()
        self.draw_keys()
        self.draw_gameboard()

    def draw_title(self):
        title = Turtle()
        title.penup()
        title.hideturtle()
        title.pencolor("white")
        title.goto(0, 300)
        title.pendown()
        title.write("TETRIS", align = ALIGN, font = FONT)

    def draw_keys(self):
        key = Turtle()
        key.penup()
        key.hideturtle()
        key.pencolor("white")
        key.goto(210, 300)
        key.pendown()
        key.write("Next", align = ALIGN, font = ("Impact", 24, "normal"))
        key.penup()
        key.goto(-210, 300)
        key.pendown()
        key.write("Hold", align = ALIGN, font = ("Impact", 24, "normal"))

    def game_over(self):
        game_over_writer = Turtle()
        game_over_writer.penup()
        game_over_writer.hideturtle()
        game_over_writer.pencolor("white")
        game_over_writer.pendown()
        game_over_writer.write("GAME OVER", align=ALIGN, font=FONT)

    def draw_gameboard(self):
        layout = Turtle()
        layout.hideturtle()
        layout.pencolor("white")
        layout.penup()
        layout.goto(0, -300)
        layout.pendown()
        layout.forward(150)
        layout.goto(150, 300)
        layout.goto(-150, 300)
        layout.goto(-150, -300)
        layout.goto(0, -300)
        layout.penup()
        layout.goto(160, 300)
        layout.pendown()
        layout.goto(160, 200)
        layout.goto(260, 200)
        layout.goto(260, 300)
        layout.goto(160, 300)
        layout.penup()
        layout.goto(160, 190)
        layout.pendown()
        layout.goto(235, 190)
        layout.goto(235, 115)
        layout.goto(160, 115)
        layout.goto(160, 190)
        layout.penup()
        layout.goto(160, 105)
        layout.pendown()
        layout.goto(235, 105)
        layout.goto(235, 30)
        layout.goto(160, 30)
        layout.goto(160, 105)
        layout.penup()
        layout.goto(-160, 300)
        layout.pendown()
        layout.goto(-260, 300)
        layout.goto(-260, 200)
        layout.goto(-160, 200)
        layout.goto(-160, 300)