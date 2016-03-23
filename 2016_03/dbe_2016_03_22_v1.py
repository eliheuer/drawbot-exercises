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
num_frames = 63

# gird variables
origin = (128, 128)
width = 256
height = 256
center = width/2
num_x_units = 8
num_y_units = 8

#type
type_x_pos = 0 
type_y_pos = 0
type_step = 0 

def new_page(): 
    newPage(canvas, canvas) 
    frameDuration(1/24) 
    fill(0.8) 
    rect(0, 0, canvas, canvas) 

def type(type_x_pos, type_y_pos):
    fill(1, 0.5, 0.3)
    strokeWidth(2)
    stroke(0.2, 0.3, 0.4)
    fontSize(32)
    font("Helvetica neue")
    text("Hello World", (24, 24))
       
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
    translate(128, 128)
    type(type_x_pos, type_y_pos)
    type_step += 0.1
    
    fill(1)
    strokeWidth(2)
    stroke(0)
    fontSize(32)
    font("Helvetica neue")
    text("Hello World", (-124, -124))
    
saveImage("dbe_2016_03_22_v1.gif")