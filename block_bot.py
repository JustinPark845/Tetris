from turtle import Screen
import keyboard
from blocks import Blocks
from upcoming_and_hold import Up, Hold
from line_breaker import LineBreaker
import time
import random

block_list = ["i", "t", "s", "z", "j", "l", "o"]

class Block_Bot(Blocks):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.screen = Screen()
        self.blocks = Blocks()
        self.up = Up()
        self.hold = Hold()
        self.line_breaker = LineBreaker()
        self.already_saved = False
        self.direction = 0
        self.block_bag = ["i", "t", "s", "z", "j", "l", "o"]
        self.saved_block = []
        self.next_block_list = []
        self.permanent_stamp_id_list = []
        self.permanent_stamp_pos_id_list = []
        self.permanent_stamp_bottom_pos_id_list = [(-135,-315), (-105,-315), (-75,-315), (-45,-315), (-15,-315), (15,-315), (45,-315), (75,-315), (105,-315), (135,-315)]
        self.side_permanent_stamp_pos_id_list = [(-165,-315),(-165,285),(165,285),(-165,-285),(-165,-255),(-165,-225),(-165,-195),(-165,-165),(-165,-135),(-165,-105),(-165,-75),(-165,-45),(-165,-15),(-165,15),(-165,45),(-165,75),(-165,105),(-165,135),(-165,165),(-165,195),(-165,225),(-165,255),(165,-315),(165,-285),(165,-255),(165,-225),(165,-195),(165,-165),(165,-135),(165,-105),(165,-75),(165,-45),(165,-15),(165,15),(165,45),(165,75),(165,105),(165,135),(165,165),(165,195),(165,225),(165,255)]
        self.beginning_blocks()

    #used methods
    def beginning_blocks(self):
        for i in range(4):
            starting_blocks = random.sample(self.block_bag, 1)
            self.block_bag.remove(starting_blocks[0])
            self.next_block_list.extend(starting_blocks)

    def block_under(self):
        true_false_list = []
        aggregate_list = self.permanent_stamp_bottom_pos_id_list + self.permanent_stamp_pos_id_list
        for temp_coords in self.blocks.stamp_pos_id_list:
            for perm_coords in aggregate_list:
                true_false_list.append(round(temp_coords[0],0) == round(perm_coords[0],0) and round(temp_coords[1],0) == round(perm_coords[1],0) + 30)
        if True in true_false_list:
            return True
        else:
            return False

    def block_printer(self):
        self.blocks.block_methods[self.next_block_list[0]](self.blocks)

    def clear_new_id(self):
        for i in range(4):
            self.blocks.clearstamp(self.blocks.stamp_id_list[0])
            self.blocks.stamp_id_list.pop(0)
            self.blocks.stamp_pos_id_list.pop(0)
            if self.next_block_list[0] == "o" and len(self.blocks.yellow_blocks) != 0:
                self.blocks.yellow_blocks = self.blocks.yellow_blocks[:-1]
            if self.next_block_list[0] == "l" and len(self.blocks.orange_blocks) != 0:
                self.blocks.orange_blocks = self.blocks.orange_blocks[:-1]
            if self.next_block_list[0] == "j" and len(self.blocks.blue_blocks) != 0:
                self.blocks.blue_blocks = self.blocks.blue_blocks[:-1]
            if self.next_block_list[0] == "i" and len(self.blocks.light_blue_blocks) != 0:
                self.blocks.light_blue_blocks = self.blocks.light_blue_blocks[:-1]
            if self.next_block_list[0] == "s" and len(self.blocks.green_blocks) != 0:
                self.blocks.green_blocks = self.blocks.green_blocks[:-1]
            if self.next_block_list[0] == "z" and len(self.blocks.red_blocks) != 0:
                self.blocks.red_blocks = self.blocks.red_blocks[:-1]
            if self.next_block_list[0] == "t" and len(self.blocks.purple_blocks) != 0:
                self.blocks.purple_blocks = self.blocks.purple_blocks[:-1]
            print("---------------------------------------")
            print(self.blocks.yellow_blocks)
            print(self.blocks.orange_blocks)
            print(self.blocks.blue_blocks)
            print(self.blocks.light_blue_blocks)
            print(self.blocks.green_blocks)
            print(self.blocks.red_blocks)
            print(self.blocks.purple_blocks)
    def block_selector(self):
        additional_block = random.sample(self.block_bag, 1)
        self.block_bag.remove(additional_block[0])
        self.next_block_list.extend(additional_block)
        if len(self.block_bag) == 0:
            self.block_bag = ["i", "t", "s", "z", "j", "l", "o"]


    #game
    def game_progressor(self):
        print("-------------------------------------------")
        print(self.blocks.yellow_blocks)
        print(self.blocks.orange_blocks)
        print(self.blocks.blue_blocks)
        print(self.blocks.light_blue_blocks)
        print(self.blocks.green_blocks)
        print(self.blocks.red_blocks)
        print(self.blocks.purple_blocks)
        self.up.draw_sidebar(self.next_block_list)
        while True:
            self.block_printer()
            times = 120
            for i in range(times):
                if keyboard.is_pressed("left"):
                    self.move_left()
                if keyboard.is_pressed("right"):
                    self.move_right()
                if keyboard.is_pressed("up"):
                    if self.next_block_list[0] != "o":
                        self.rotate()
                if keyboard.is_pressed("down"):
                    break
                if keyboard.is_pressed("space"):
                    self.instant_place()
                if keyboard.is_pressed("z"):
                    if self.already_saved == False:
                        self.already_saved = True
                        self.save_piece()
                        self.screen.update()
                    else:
                        time.sleep(0.005)
                else:
                    time.sleep(0.005)

            if self.next_block_list[0] == "i":
                self.i_movement()
            if self.next_block_list[0] == "t":
                self.t_movement()
            if self.next_block_list[0] == "s":
                self.s_movement()
            if self.next_block_list[0] == "z":
                self.z_movement()
            if self.next_block_list[0] == "j":
                self.j_movement()
            if self.next_block_list[0] == "l":
                self.l_movement()
            if self.next_block_list[0] == "o":
                self.o_movement()

            if self.block_under():
                for i in range(4):
                    self.permanent_stamp_id_list.append(self.blocks.stamp_id_list[0])
                    self.permanent_stamp_pos_id_list.append(self.blocks.stamp_pos_id_list[0])
                    self.side_permanent_stamp_pos_id_list.append(self.blocks.stamp_pos_id_list[0])
                    self.blocks.stamp_id_list.pop(0)
                    self.blocks.stamp_pos_id_list.pop(0)
                    if self.line_breaker.check_if_line_filled(self.permanent_stamp_pos_id_list,self.permanent_stamp_id_list,
                                                        self.blocks.yellow_blocks,self.blocks.orange_blocks,self.blocks.blue_blocks,
                                                        self.blocks.light_blue_blocks,self.blocks.green_blocks,self.blocks.red_blocks,
                                                        self.blocks.purple_blocks) == True:                             
                        self.blocks.clearstamps()
                        self.line_breaker.color_printer(self.line_breaker.temporary_stamp_coord_dictionary)
                break
            self.screen.update()
            self.clear_new_id()
        self.blocks.setheading(0)
        self.direction = 0
        self.next_block_list.pop(0)
        self.block_selector()
        self.already_saved = False

    #conditional
    def game_over(self):
        for height in self.permanent_stamp_pos_id_list:
            if round(height[1],0) == 285:
                return True

    #player input
    def s_z_rotate_bound(self):
        rotate_bound_list = []
        for temp_coords in self.blocks.stamp_pos_id_list:
            for perm_coords in self.side_permanent_stamp_pos_id_list:
                rotate_bound_list.append(round(temp_coords[0],0) == round(perm_coords[0],0))
        if True in rotate_bound_list:
            return True
        else:
            return False

    def rotate_bound(self):
        rotate_bound_list = []
        for temp_coords in self.blocks.stamp_pos_id_list:
            for perm_coords in self.side_permanent_stamp_pos_id_list:
                rotate_bound_list.append(round(temp_coords[1],0) == round(perm_coords[1],0) and round(temp_coords[0],0) == round(perm_coords[0],0))
        if True in rotate_bound_list:
            return True
        else:
            return False

    def rotate(self):
        if self.next_block_list[0] == "s" or self.next_block_list[0] == "z":
            if self.direction == 0:
                self.blocks.forward(30)
                self.blocks.setheading(270)
                self.direction = self.blocks.heading()
                self.block_printer()
                self.clear_new_id()
                self.screen.update()
                time.sleep(0.1)
            elif self.direction == 270:
                self.blocks.setheading(0)
                self.direction = self.blocks.heading()
                self.block_printer()
                self.clear_new_id()
                if self.s_z_rotate_bound():
                    self.direction = self.blocks.heading()
                    self.blocks.setheading(0)
                    self.blocks.forward(30)
                    self.blocks.setheading(self.direction)
                    self.block_printer()
                    self.clear_new_id()
                self.screen.update()
                time.sleep(0.1)
        if self.next_block_list[0] == "t":
            self.blocks.forward(30)
            self.blocks.rt(90)
            self.direction = self.blocks.heading()
            self.block_printer()
            self.clear_new_id()
            if self.rotate_bound():
                if self.blocks.heading() == 180:
                    self.blocks.back(30)
                    self.direction = self.blocks.heading()
                    self.blocks.setheading(90)
                    self.blocks.back(30)
                    self.blocks.setheading(self.direction)
                    self.block_printer()
                    self.clear_new_id()
                else:
                    self.blocks.back(30)
                    self.block_printer()
                    self.clear_new_id()
            self.screen.update()
            time.sleep(0.1)
        if self.next_block_list[0] == "j" or self.next_block_list[0] == "l":
            self.blocks.forward(30)
            self.blocks.rt(90)
            self.direction = self.blocks.heading()
            self.block_printer()
            self.clear_new_id()
            if self.rotate_bound():
                if self.blocks.heading() == 180:
                    self.blocks.back(30)
                    self.direction = self.blocks.heading()
                    self.blocks.setheading(90)
                    self.blocks.back(30)
                    self.blocks.setheading(self.direction)
                    self.block_printer()
                    self.clear_new_id()
                else:
                    self.blocks.back(30)
                    self.block_printer()
                    self.clear_new_id()
            self.screen.update()
            time.sleep(0.1)
        if self.next_block_list[0] == "i":
            if self.blocks.heading() == 0:
                self.blocks.setheading(270)
                self.direction = 270
                self.block_printer()
                self.clear_new_id()
            else:
                self.blocks.setheading(0)
                self.direction = 0
                self.block_printer()
                self.clear_new_id()
                if self.rotate_bound():
                    self.blocks.forward(30)
                    self.block_printer()
                    self.clear_new_id()
                    if self.rotate_bound():
                        self.blocks.back(90)
                self.blocks.setheading(0)
                self.block_printer()
                self.clear_new_id()
            self.screen.update()
            time.sleep(0.1)

    def left_bound(self):
        left_bound_list = []
        for temp_coords in self.blocks.stamp_pos_id_list:
            for perm_coords in self.side_permanent_stamp_pos_id_list:
                left_bound_list.append(round(temp_coords[1],0) == round(perm_coords[1],0) and round(temp_coords[0],0) == round(perm_coords[0],0) + 30)
        if True in left_bound_list:
            return True
        else:
            return False

    def move_left(self):
        if not self.left_bound():
            if self.next_block_list[0] == "i":
                self.blocks.setheading(180)
                self.blocks.forward(30)
                self.blocks.setheading(self.direction)
                self.block_printer()
                self.clear_new_id()
                self.screen.update()
                time.sleep(0.075)
                print("---------------------------------------")
                print(self.blocks.yellow_blocks)
                print(self.blocks.orange_blocks)
                print(self.blocks.blue_blocks)
                print(self.blocks.light_blue_blocks)
                print(self.blocks.green_blocks)
                print(self.blocks.red_blocks)
                print(self.blocks.purple_blocks)
            elif self.next_block_list[0] == "o":
                self.blocks.back(30)
                self.block_printer()
                self.clear_new_id()
                self.screen.update()
                time.sleep(0.075)
            else:
                if self.direction == 0:
                    self.blocks.back(30)
                    self.blocks.lt(90)
                    self.blocks.forward(30)
                    self.blocks.rt(90)
                    self.block_printer()
                    self.clear_new_id()
                    self.screen.update()
                    time.sleep(0.075)
                if self.direction == 90:
                    self.blocks.lt(90)
                    self.blocks.forward(60)
                    self.blocks.rt(90)
                    self.block_printer()
                    self.clear_new_id()
                    self.screen.update()
                    time.sleep(0.075)
                if self.direction == 180:
                    self.blocks.forward(30)
                    self.blocks.lt(90)
                    self.blocks.forward(30)
                    self.blocks.rt(90)
                    self.block_printer()
                    self.clear_new_id()
                    self.screen.update()
                    time.sleep(0.075)
                if self.direction == 270:
                    self.block_printer()
                    self.clear_new_id()
                    self.screen.update()
                    time.sleep(0.075)

    def right_bound(self):
        right_bound_list = []
        for temp_coords in self.blocks.stamp_pos_id_list:
            for perm_coords in self.side_permanent_stamp_pos_id_list:
                right_bound_list.append(round(temp_coords[1],0) == round(perm_coords[1],0) and round(temp_coords[0],0) == round(perm_coords[0],0) - 30)
        if True in right_bound_list:
            return True
        else:
            return False

    def move_right(self):
        if not self.right_bound():
            if self.next_block_list[0] == "i":
                self.blocks.setheading(0)
                self.blocks.forward(30)
                self.blocks.setheading(self.direction)
                self.block_printer()
                self.clear_new_id()
                self.screen.update()
                time.sleep(0.075)
            elif self.next_block_list[0] == "o":
                self.blocks.forward(30)
                self.block_printer()
                self.clear_new_id()
                self.screen.update()
                time.sleep(0.075)
            else:
                if self.direction == 0:
                    self.blocks.forward(30)
                    self.blocks.lt(90)
                    self.blocks.forward(30)
                    self.blocks.rt(90)
                    self.block_printer()
                    self.clear_new_id()
                    self.screen.update()
                    time.sleep(0.075)
                if self.direction == 90:
                    self.block_printer()
                    self.clear_new_id()
                    self.screen.update()
                    time.sleep(0.075)
                if self.direction == 180:
                    self.blocks.back(30)
                    self.blocks.lt(90)
                    self.blocks.forward(30)
                    self.blocks.rt(90)
                    self.block_printer()
                    self.clear_new_id()
                    self.screen.update()
                    time.sleep(0.075)
                if self.direction == 270:
                    self.blocks.lt(90)
                    self.blocks.forward(60)
                    self.blocks.rt(90)
                    self.block_printer()
                    self.clear_new_id()
                    self.screen.update()
                    time.sleep(0.075)

    def instant_place(self):
        while self.block_under() == False:
            if self.next_block_list[0] == "i":
                self.i_movement()
            if self.next_block_list[0] == "t":
                self.t_movement()
            if self.next_block_list[0] == "s":
                self.s_movement()
            if self.next_block_list[0] == "z":
                self.z_movement()
            if self.next_block_list[0] == "j":
                self.j_movement()
            if self.next_block_list[0] == "l":
                self.l_movement()
            if self.next_block_list[0] == "o":
                self.blocks.setheading(0)
                self.o_movement()
            self.block_printer()
            self.clear_new_id()
            self.screen.update()
        time.sleep(0.1)

    def save_piece(self):
        for i in range(4):
            if self.next_block_list[0] == "o" and len(self.blocks.yellow_blocks) != 0:
                self.blocks.yellow_blocks = self.blocks.yellow_blocks[:-1]
            if self.next_block_list[0] == "l" and len(self.blocks.orange_blocks) != 0:
                self.blocks.orange_blocks = self.blocks.orange_blocks[:-1]
            if self.next_block_list[0] == "j" and len(self.blocks.blue_blocks) != 0:
                self.blocks.blue_blocks = self.blocks.blue_blocks[:-1]
            if self.next_block_list[0] == "i" and len(self.blocks.light_blue_blocks) != 0:
                self.blocks.light_blue_blocks = self.blocks.light_blue_blocks[:-1]
            if self.next_block_list[0] == "s" and len(self.blocks.green_blocks) != 0:
                self.blocks.green_blocks = self.blocks.green_blocks[:-1]
            if self.next_block_list[0] == "z" and len(self.blocks.red_blocks) != 0:
                self.blocks.red_blocks = self.blocks.red_blocks[:-1]
            if self.next_block_list[0] == "t" and len(self.blocks.purple_blocks) != 0:
                self.blocks.purple_blocks = self.blocks.purple_blocks[:-1]
        if len(self.saved_block) == 0:
            self.saved_block.append(self.next_block_list[0])
            del self.next_block_list[0]
            self.block_selector()
            self.hold.draw_savepiece(self.saved_block)
            self.up.draw_sidebar(self.next_block_list)
            self.blocks.goto(-15,285)
            self.blocks.setheading(0)
            self.screen.update()
        else:
            for i in range(4):
                if self.next_block_list[0] == "o" and len(self.blocks.yellow_blocks) != 0:
                    self.blocks.yellow_blocks = self.blocks.yellow_blocks[:-1]
                if self.next_block_list[0] == "l" and len(self.blocks.orange_blocks) != 0:
                    self.blocks.orange_blocks = self.blocks.orange_blocks[:-1]
                if self.next_block_list[0] == "j" and len(self.blocks.blue_blocks) != 0:
                    self.blocks.blue_blocks = self.blocks.blue_blocks[:-1]
                if self.next_block_list[0] == "i" and len(self.blocks.light_blue_blocks) != 0:
                    self.blocks.light_blue_blocks = self.blocks.light_blue_blocks[:-1]
                if self.next_block_list[0] == "s" and len(self.blocks.green_blocks) != 0:
                    self.blocks.green_blocks = self.blocks.green_blocks[:-1]
                if self.next_block_list[0] == "z" and len(self.blocks.red_blocks) != 0:
                    self.blocks.red_blocks = self.blocks.red_blocks[:-1]
                if self.next_block_list[0] == "t" and len(self.blocks.purple_blocks) != 0:
                    self.blocks.purple_blocks = self.blocks.purple_blocks[:-1]
            fodder_list = []
            fodder_list.append(self.saved_block[0])
            del self.saved_block[0]
            self.saved_block.append(self.next_block_list[0])
            self.next_block_list[0] = fodder_list[0]
            self.block_selector()
            self.hold.draw_savepiece(self.saved_block)
            self.blocks.goto(-15,285)
            self.blocks.setheading(0)
            self.screen.update()

    #block movement
    def i_movement(self):
        #east
        if self.direction == 0:
            self.blocks.rt(90)
            self.blocks.forward(30)
            self.blocks.lt(90)
        #north
        if self.direction == 90:
            self.blocks.back(30)
        #west
        if self.direction == 180:
            self.blocks.lt(90)
            self.blocks.forward(30)
            self.blocks.rt(90)
        #south
        if self.direction == 270:
            self.blocks.forward(30)

    def t_movement(self):
        #east
        if self.direction == 0:
            pass
        #north
        if self.direction == 90:
            self.blocks.rt(90)
            self.blocks.back(30)
            self.blocks.lt(90)
            self.blocks.back(30)
        #west
        if self.direction == 180:
            self.blocks.lt(90)
            self.blocks.forward(60)
            self.blocks.rt(90)
        #south
        if self.direction == 270:
            self.blocks.lt(90)
            self.blocks.forward(30)
            self.blocks.rt(90)
            self.blocks.forward(30)

    def s_movement(self):
        #east
        if self.direction == 0:
            pass
        #south
        if self.direction == 270:
            self.blocks.lt(90)
            self.blocks.forward(30)
            self.blocks.rt(90)
            self.blocks.forward(30)
    
    def z_movement(self):
        #east
        if self.direction == 0:
            pass
        #south
        if self.direction == 270:
            self.blocks.lt(90)
            self.blocks.forward(30)
            self.blocks.rt(90)
            self.blocks.forward(30)

    def j_movement(self):
        #east
        if self.direction == 0:
            pass
        #north
        if self.direction == 90:
            self.blocks.rt(90)
            self.blocks.back(30)
            self.blocks.lt(90)
            self.blocks.back(30)
        #west
        if self.direction == 180:
            self.blocks.lt(90)
            self.blocks.forward(60)
            self.blocks.rt(90)
        #south
        if self.direction == 270:
            self.blocks.lt(90)
            self.blocks.forward(30)
            self.blocks.rt(90)
            self.blocks.forward(30)

    def l_movement(self):
        #east
        if self.direction == 0:
            pass
        #north
        if self.direction == 90:
            self.blocks.rt(90)
            self.blocks.back(30)
            self.blocks.lt(90)
            self.blocks.back(30)
        #west
        if self.direction == 180:
            self.blocks.lt(90)
            self.blocks.forward(60)
            self.blocks.rt(90)
        #south
        if self.direction == 270:
            self.blocks.lt(90)
            self.blocks.forward(30)
            self.blocks.rt(90)
            self.blocks.forward(30)

    def o_movement(self):
        self.blocks.rt(90)
        self.blocks.forward(30)
        self.blocks.lt(90)