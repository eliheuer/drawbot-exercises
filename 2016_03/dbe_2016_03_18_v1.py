#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#  
#                                                                             #
#  Eli Heuer's daily DrawBot exercise!                                        #
#                                                                             #
#  WWW: https://www.tumblr.com/blog/drawbot-exercises                         #
#  Mail: eliheuer@gmail.com                                                   #
#  Drawn on: 03/18/16 -- version 1                                            #
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

# path variables
path_x = 0
path_y = 0
divisions = 0

# box variables
box_size_x = 32
box_size_y = 32
box_amp = 24
box_step = 0
box_count = 100
box_rt = 2

def new_page(): 
    newPage(canvas, canvas) 
    frameDuration(1/24) 
    fill(0.8) 
    rect(0, 0, canvas, canvas) 
        
def box(x_pos, y_pos, box_size_x, box_size_y):
    fill(1)
    strokeWidth(1)
    stroke(0.1)
    rotate(6)
    rect((x_pos - 2) + center/2, (y_pos - 2) + center/2, 
        box_size_x, box_size_y)
    
def draw_path(path_x, path_y, box_count, dot_amp, box_step):  
    for segment in range(box_count):
        box_x = math.cos(box_step) * box_amp
        box_y = math.sin(box_step) * box_amp
        box(box_x, box_y, box_size_x, box_size_y)
        box_step += 0.1 * math.pi
       
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
    draw_path(path_x, path_y, box_count, box_amp, box_step)
    box_step += 0.1
    
saveImage("dbe_2016_03_18_v1.gif")