from turtle import Turtle
from blocks import Blocks
import time

class LineBreaker(Blocks):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.yellow_ink = Turtle()
        self.yellow_ink.hideturtle()
        self.orange_ink = Turtle()
        self.orange_ink.hideturtle()
        self.blue_ink = Turtle()
        self.blue_ink.hideturtle()
        self.light_blue_ink = Turtle()
        self.light_blue_ink.hideturtle()
        self.green_ink = Turtle()
        self.green_ink.hideturtle()
        self.red_ink = Turtle()
        self.red_ink.hideturtle()
        self.purple_ink = Turtle()
        self.purple_ink.hideturtle()
        self.row_coordinate_list = []
        self.sustained_row_coordinate_list = []
        self.temporary_stamp_coord_dictionary = {}

    def check_if_line_filled(self,pos_id_list,id_list,yellow,orange,blue,light_blue,green,red,purple):
        y_coords_input = -285
        number_of_lines_cleared = 0
        while y_coords_input <= 255:
            self.required_coordinates(y_coords_input)
            self.sustained_row_coordinate_list.clear()
            self.sustained_row_coordinate_list.extend(self.row_coordinate_list)
            for coords in pos_id_list:
                whole_x_coord = round(coords[0],0)
                whole_y_coord = round(coords[1],0)
                whole_coords = (whole_x_coord,whole_y_coord)
                if whole_coords in self.row_coordinate_list:
                    self.row_coordinate_list.remove(whole_coords)
            if len(self.row_coordinate_list) == 0:
                number_of_lines_cleared += 1
                self.clear_line(y_coords_input)
                self.remaining_stamp_coords(yellow,orange,blue,light_blue,green,red,purple,pos_id_list,id_list)
                self.lower_remaining_stamp_coords(y_coords_input,yellow,orange,blue,light_blue,green,red,purple,pos_id_list)
                return(True)
            self.row_coordinate_list = []
            y_coords_input = round(y_coords_input+30,0)

    def required_coordinates(self,y_coord):
        x_coord = -135
        required_coordinates_list = []
        while x_coord <= 135:
            required_coordinates_list.append((x_coord,y_coord))
            x_coord = round(x_coord+30,0)
        self.row_coordinate_list = required_coordinates_list

    def clear_line(self,floor_number):
        x_coord = -135
        clear_line = Turtle()
        clear_line.hideturtle()
        clear_line.penup()
        clear_line.goto(-135,floor_number)
        clear_line.color("black")
        clear_line.stamp()
        for black in range(9):
            clear_line.forward(30)
            clear_line.stamp()

    def remaining_stamp_coords(self,yellow,orange,blue,light_blue,green,red,purple,stamp_pos_id,stamp_id):
        for coords in self.sustained_row_coordinate_list:
            for count,b_coords in enumerate(stamp_pos_id):
                whole_x_coord = round(b_coords[0],0)
                whole_y_coord = round(b_coords[1],0)
                whole_coords = (whole_x_coord,whole_y_coord)
                if coords == whole_coords:
                    stamp_pos_id.remove(b_coords)
                    count = count - 1
            for count,b_coords in enumerate(yellow):
                whole_x_coord = round(b_coords[0],0)
                whole_y_coord = round(b_coords[1],0)
                whole_coords = (whole_x_coord,whole_y_coord)
                if coords == whole_coords:
                    yellow.remove(b_coords)
                    count = count - 1
            for count,b_coords in enumerate(orange):
                whole_x_coord = round(b_coords[0],0)
                whole_y_coord = round(b_coords[1],0)
                whole_coords = (whole_x_coord,whole_y_coord)
                if coords == whole_coords:
                    orange.remove(b_coords)
                    count = count - 1
            for count,b_coords in enumerate(blue):
                whole_x_coord = round(b_coords[0],0)
                whole_y_coord = round(b_coords[1],0)
                whole_coords = (whole_x_coord,whole_y_coord)
                if coords == whole_coords:
                    blue.remove(b_coords)
                    count = count - 1
            for count,b_coords in enumerate(light_blue):
                whole_x_coord = round(b_coords[0],0)
                whole_y_coord = round(b_coords[1],0)
                whole_coords = (whole_x_coord,whole_y_coord)
                if coords == whole_coords:
                    light_blue.remove(b_coords)
                    count = count - 1
            for count,b_coords in enumerate(green):
                whole_x_coord = round(b_coords[0],0)
                whole_y_coord = round(b_coords[1],0)
                whole_coords = (whole_x_coord,whole_y_coord)
                if coords == whole_coords:
                    green.remove(b_coords)
                    count = count - 1
            for count,b_coords in enumerate(red):
                whole_x_coord = round(b_coords[0],0)
                whole_y_coord = round(b_coords[1],0)
                whole_coords = (whole_x_coord,whole_y_coord)
                if coords == whole_coords:
                    red.remove(b_coords)
                    count = count - 1
            for count,b_coords in enumerate(purple):
                whole_x_coord = round(b_coords[0],0)
                whole_y_coord = round(b_coords[1],0)
                whole_coords = (whole_x_coord,whole_y_coord)
                if coords == whole_coords:
                    purple.remove(b_coords)
                    count = count - 1

    def lower_remaining_stamp_coords(self,height,yellow,orange,blue,light_blue,green,red,purple,s_pos):
        for count in range(len(s_pos)):
            s_pos.pop(0)
        for count,coordinates in enumerate(yellow):
            if coordinates[1] > height:
                yellow[count] = (round(coordinates[0],0),round(coordinates[1]-30,0))
            else:
                pass
        for count,coordinates in enumerate(orange):
            if coordinates[1] > height:
                orange[count] = (round(coordinates[0],0),round(coordinates[1]-30,0))
            else:
                pass
        for count,coordinates in enumerate(blue):
            if coordinates[1] > height:
                blue[count] = (round(coordinates[0],0),round(coordinates[1]-30,0))
            else:
                pass
        for count,coordinates in enumerate(light_blue):
            if coordinates[1] > height:
                light_blue[count] = (round(coordinates[0],0),round(coordinates[1]-30,0))
            else:
                pass
        for count,coordinates in enumerate(green):
            if coordinates[1] > height:
                green[count] = (round(coordinates[0],0),round(coordinates[1]-30,0))
            else:
                pass
        for count,coordinates in enumerate(red):
            if coordinates[1] > height:
                red[count] = (round(coordinates[0],0),round(coordinates[1]-30,0))
            else:
                pass
        for count,coordinates in enumerate(purple):
            if coordinates[1] > height:
                purple[count] = (round(coordinates[0],0),round(coordinates[1]-30,0))
            else:
                pass
        self.record_remaining_stamp_coords(yellow,orange,blue,light_blue,green,red,purple,s_pos)

    def record_remaining_stamp_coords(self,yellow,orange,blue,light_blue,green,red,purple,s_pos):
        self.temporary_stamp_coord_dictionary.clear()
        self.temporary_stamp_coord_dictionary["yellow"] = []
        self.temporary_stamp_coord_dictionary["orange"] = []
        self.temporary_stamp_coord_dictionary["blue"] = []
        self.temporary_stamp_coord_dictionary["light_blue"] = []
        self.temporary_stamp_coord_dictionary["green"] = []
        self.temporary_stamp_coord_dictionary["red"] = []
        self.temporary_stamp_coord_dictionary["purple"] = []
        for i in range(len(yellow)):
            self.temporary_stamp_coord_dictionary["yellow"].append(yellow[i])
            s_pos.append(yellow[i])
        for i in range(len(orange)):
            self.temporary_stamp_coord_dictionary["orange"].append(orange[i])
            s_pos.append(orange[i])
        for i in range(len(blue)):
            self.temporary_stamp_coord_dictionary["blue"].append(blue[i])
            s_pos.append(blue[i])
        for i in range(len(light_blue)):
            self.temporary_stamp_coord_dictionary["light_blue"].append(light_blue[i])
            s_pos.append(light_blue[i])
        for i in range(len(green)):
            self.temporary_stamp_coord_dictionary["green"].append(green[i])
            s_pos.append(green[i])
        for i in range(len(red)):
            self.temporary_stamp_coord_dictionary["red"].append(red[i])
            s_pos.append(red[i])
        for i in range(len(purple)):
            self.temporary_stamp_coord_dictionary["purple"].append(purple[i])
            s_pos.append(purple[i])
        print(self.temporary_stamp_coord_dictionary)

    def color_printer(self,blueprint):
        self.yellow_ink.clearstamps()
        self.yellow_ink.penup()
        self.yellow_ink.color("yellow")
        self.yellow_ink.shape("square")
        self.yellow_ink.shapesize(1.4, 1.4, 1.4)
        for coordinates in blueprint["yellow"]:
            self.yellow_ink.goto(coordinates)
            self.yellow_ink.stamp()
        self.orange_ink.clearstamps()
        self.orange_ink.penup()
        self.orange_ink.color("orange")
        self.orange_ink.shape("square")
        self.orange_ink.shapesize(1.4, 1.4, 1.4)
        for coordinates in blueprint["orange"]:
            self.orange_ink.goto(coordinates)
            self.orange_ink.stamp()
        self.blue_ink.clearstamps()
        self.blue_ink.penup()
        self.blue_ink.color("blue")
        self.blue_ink.shape("square")
        self.blue_ink.shapesize(1.4, 1.4, 1.4)
        for coordinates in blueprint["blue"]:
            self.blue_ink.goto(coordinates)
            self.blue_ink.stamp()
        self.light_blue_ink.clearstamps()
        self.light_blue_ink.penup()
        self.light_blue_ink.color("light blue")
        self.light_blue_ink.shape("square")
        self.light_blue_ink.shapesize(1.4, 1.4, 1.4)
        for coordinates in blueprint["light_blue"]:
            self.light_blue_ink.goto(coordinates)
            self.light_blue_ink.stamp()
        self.green_ink.clearstamps()
        self.green_ink.penup()
        self.green_ink.color("green")
        self.green_ink.shape("square")
        self.green_ink.shapesize(1.4, 1.4, 1.4)
        for coordinates in blueprint["green"]:
            self.green_ink.goto(coordinates)
            self.green_ink.stamp()
        self.red_ink.clearstamps()
        self.red_ink.penup()
        self.red_ink.color("red")
        self.red_ink.shape("square")
        self.red_ink.shapesize(1.4, 1.4, 1.4)
        for coordinates in blueprint["red"]:
            self.red_ink.goto(coordinates)
            self.red_ink.stamp()
        self.purple_ink.clearstamps()
        self.purple_ink.penup()
        self.purple_ink.color("purple")
        self.purple_ink.shape("square")
        self.purple_ink.shapesize(1.4, 1.4, 1.4)
        for coordinates in blueprint["purple"]:
            self.purple_ink.goto(coordinates)
            self.purple_ink.stamp()
        