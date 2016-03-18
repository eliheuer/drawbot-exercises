#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#  
#                                                                             #
#  Eli Heuer's daily DrawBot exercise!                                        #
#                                                                             #
#  WWW: https://www.tumblr.com/blog/drawbot-exercises                         #
#  Mail: eliheuer@gmail.com                                                   #
#  Drawn on: 03/16/17 -- version 1                                            #
#  Made with DrawBot: http://www.drawbot.com/                                 #
#                                                                             #
#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#

# from drawBot import * # uncomment if using setupAsModule.py
import math 
from itertools import cycle, chain, repeat

# static variables
canvas = 512 
num_frames = 100 

# gird variables
origin = (128, 128)
width = 256
height = 256
center = width/2
num_x_units = 7
num_y_units = 7

# path variables
path_x = 0
path_y = 0
divisions = 0

# box variables
box_size_x = 36 
box_size_y = 36
box_amp = 110
box_step = 0
box_count = 1
box_rt = 0

# draws a new frame in the animation
def new_page(): 
    newPage(canvas, canvas) 
    frameDuration(1/24) 
    fill(0.8) 
    rect(0, 0, canvas, canvas) 

# draws the dot from two position variables    
def box(x_pos, y_pos, box_size_x, box_size_y, box_rt):
    fill(1)
    strokeWidth(1)
    stroke(0.2)
    rotate(box_rt)
    rect((x_pos - 2) + center, (y_pos - 2) + center, box_size_x, box_size_y)
    
# draws a circle from 5 arguments, see 'gird variables' above
def draw_path(path_x, path_y, box_count, dot_amp, box_step, box_rt):
     
    for segment in range(box_count):
        box_x = math.cos(box_step) * box_amp
        box_y = math.sin(box_step) * box_amp
        box(box_x, box_y, box_size_x, box_size_y, box_rt)
        
        box_step += 0.2 * math.pi
       
# draws a grid from given arguments    
def grid(origin, width, height, num_x_units, num_y_units):
    translate(*origin)
    strokeWidth(2)
    stroke(0.3) 
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

# draw each frame as a new page

for frame in range(num_frames):
    new_page()
    grid(origin, width, height, num_x_units, num_y_units)
    translate(-16, -16)
    draw_path(path_x, path_y, box_count, box_amp, box_step, box_rt)
    box_count_string = "{:03d}".format(box_count)
    #box_count += 4
    box_step += 0.1
    box_rt += 0.01
    
saveImage("dbe_2016_03_17_v1.gif")