#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#  
#                                                                             #
#  Eli Heuer's daily DrawBot exercise!                                        #
#                                                                             #
#  WWW: https://www.tumblr.com/blog/drawbot-exercises                         #
#  Mail: eliheuer@gmail.com                                                   #
#  Drawn on: 03/23/16 -- version 1                                            #
#  Made with DrawBot: http://www.drawbot.com/                                 #
#                                                                             #
#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#

# from drawBot import * # uncomment if using setupAsModule.py
import math
import itertools  

# static variables
canvas = 512 
num_frames = 58

# gird variables
origin = (32, 32)
width = 448 - 128
height = 448
center = width/2
num_x_units = 10
num_y_units = 14

#type
type_x_pos = 0 
type_y_pos = 0
type_step = 0 
hw_rt = 0
hw_fs = 36 * 2
hw_x_pos = 0
hw_y_pos = 0
hw_t = 0 
#itertools
type_rt_list = [0, 0, 0, 0, 0, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0, 0, 0, 0, 0, 0]
print len(type_rt_list)

type_rt_step = itertools.cycle(type_rt_list)

def new_page(): 
    newPage(canvas, canvas) 
    frameDuration(1/24) 
    fill(0.8) 
    rect(0, 0, canvas, canvas) 

def hello_world(hw_x_pos, hw_y_pos, hw_rt, hw_fs, hw_t):
    fill(0)
    hw_rt = type_rt_step.next()
    fontSize(64)
    rotate(hw_rt)
    tracking(-2.2)
    font("Helvetica neue Bold")
    text("Hello World", (-1, 0))
       
def grid(origin, width, height, num_x_units, num_y_units):
    translate(96, 32)
    strokeWidth(1)
    stroke(0.5) 
    fill(None)
    
    step_x = 0 
    unit_x = width / num_x_units
    for x in range(num_x_units + 1):
        line((step_x, 0), (step_x, height))
        step_x += unit_x
        
    step_y = 0 
    unit_y = height / num_y_units
    for y in range(num_y_units + 1):
        line((0, step_y), (width, step_y))
        step_y += unit_y
        
for frame in range(num_frames):
    new_page()
    grid(origin, width, height, num_x_units, num_y_units)
    fill(1, 0, 0)
    stroke(None)
    #oval(32, 352, 32, 32)
    translate(-2, 0)
    hello_world(hw_x_pos, hw_y_pos, hw_rt, hw_fs, hw_t)
    hw_t += 4
 
saveImage("dbe_2016_03_23_v1.gif")