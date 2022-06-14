from turtle import Turtle

class Up(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(0.75, 0.75, 0.75)
        self.shape("square")
        self.penup()
        self.speed(10)
        self.hideturtle()
        self.picture_list = []

    def draw_sidebar(self,next_block_list):
        if len(self.picture_list) == 12:
            self.clearstamps()
            self.picture_list = []
        self.goto(200,260)
        self.picture_methods[next_block_list[1]](self)
        self.goto(190,162)
        self.picture_methods[next_block_list[2]](self)
        self.goto(190,78)
        self.picture_methods[next_block_list[3]](self)

    def o_block(self):
        self.color("yellow")
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.forward(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.rt(90)
        self.forward(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.rt(90)
        self.forward(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.rt(90)
        self.forward(17.5)
        self.rt(90)

    def l_block(self):
        self.color("orange")
        self.forward(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.rt(90)
        self.forward(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.rt(90)
        self.forward(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.forward(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.rt(180)
        self.forward(17.5)

    def j_block(self):
        self.color("blue")
        self.back(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.rt(90)
        self.forward(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.lt(90)
        self.forward(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.forward(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.back(17.5)

    def i_block(self):
        self.color("light blue")
        self.back(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.forward(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.forward(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.forward(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.back(60)

    def s_block(self):
        self.color("green")
        self.forward(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.back(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.rt(90)
        self.forward(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.rt(90)
        self.forward(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.back(17.5)
        self.rt(180)

    def z_block(self):
        self.color("red")
        self.back(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.forward(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.rt(90)
        self.forward(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.lt(90)
        self.forward(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.back(17.5)

    def t_block(self):
        self.color("purple")
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.rt(90)
        self.forward(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.lt(90)
        self.forward(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.back(35)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.forward(17.5)

    picture_methods = {
        "i": i_block, 
        "t": t_block, 
        "s": s_block,
        "z": z_block,
        "j": j_block,
        "l": l_block,
        "o": o_block
    }

class Hold(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(0.75, 0.75, 0.75)
        self.shape("square")
        self.penup()
        self.speed(10)
        self.hideturtle()
        self.picture_list = []

    def draw_savepiece(self,held_block):
        if len(self.picture_list) == 4:
            self.clearstamps()
            self.picture_list = []
        self.goto(-220,260)
        self.picture_methods[held_block[0]](self)

    def o_block(self):
        self.color("yellow")
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.forward(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.rt(90)
        self.forward(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.rt(90)
        self.forward(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.rt(90)
        self.forward(17.5)
        self.rt(90)

    def l_block(self):
        self.color("orange")
        self.forward(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.rt(90)
        self.forward(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.rt(90)
        self.forward(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.forward(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.rt(180)
        self.forward(17.5)

    def j_block(self):
        self.color("blue")
        self.back(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.rt(90)
        self.forward(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.lt(90)
        self.forward(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.forward(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.back(17.5)

    def i_block(self):
        self.color("light blue")
        self.back(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.forward(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.forward(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.forward(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.back(60)

    def s_block(self):
        self.color("green")
        self.forward(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.back(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.rt(90)
        self.forward(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.rt(90)
        self.forward(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.back(17.5)
        self.rt(180)

    def z_block(self):
        self.color("red")
        self.back(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.forward(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.rt(90)
        self.forward(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.lt(90)
        self.forward(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.back(17.5)

    def t_block(self):
        self.color("purple")
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.rt(90)
        self.forward(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.lt(90)
        self.forward(17.5)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.back(35)
        stamp = self.stamp()
        self.picture_list.append(stamp)
        self.forward(17.5)

    picture_methods = {
        "i": i_block, 
        "t": t_block, 
        "s": s_block,
        "z": z_block,
        "j": j_block,
        "l": l_block,
        "o": o_block
    }