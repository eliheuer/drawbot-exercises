#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#  
#                                                                             #
#  Eli Heuer's daily DrawBot exercise!                                        #
#                                                                             #
#  WWW: https://www.tumblr.com/blog/drawbot-exercises                         #
#  Mail: eliheuer@gmail.com                                                   #
#  Drawn on: 03/22/16 -- version 1                                            #
#  Made with DrawBot: http://www.drawbot.com/                                 #
#                                                                             #
#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#

# from drawBot import * # uncomment if using setupAsModule.py
import math 

# static variables
canvas = 512 
num_frames = 36

# gird variables
origin = (32, 32)
width = 448
height = 448
center = width/2
num_x_units = 14
num_y_units = 14

#type
type_x_pos = 0 
type_y_pos = 0
type_step = 0 
hw_rt = 0
hw_fs = 36 * 2
hw_x_pos = 0
hw_y_pos = 0

def new_page(): 
    newPage(canvas, canvas) 
    frameDuration(1/4) 
    fill(0.8) 
    rect(0, 0, canvas, canvas) 

def hello_world(hw_x_pos, hw_y_pos, hw_rt, hw_fs):
    fill(0)
    fontSize(hw_fs)
    rotate(hw_rt)
    tracking(-2)
    font("Helvetica neue Bold")
    text("Hello World", (-4, 0))
       
def grid(origin, width, height, num_x_units, num_y_units):
    translate(*origin)
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
    translate(0, 0)
    hello_world(hw_x_pos, hw_y_pos, hw_rt, hw_fs)
    type_step += 1
    hw_rt += 10  

saveImage("dbe_2016_03_22_v1.gif")