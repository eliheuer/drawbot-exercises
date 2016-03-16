#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#  
#                                                                             #
#  Eli Heuer's daily DrawBot exercise!                                        #
#                                                                             #
#  WWW: https://www.tumblr.com/blog/drawbot-exercises                         #
#  Mail: eliheuer@gmail.com                                                   #
#  Drawn on: 03/16/16 -- version 1                                            #
#  Made with DrawBot: http://www.drawbot.com/                                 #
#                                                                             #
#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#

# from drawBot import * # uncomment if using setupAsModule.py
import math # for cos, sin and pi functions
from itertools import cycle, chain, repeat

# static variables
canvas = 512  # size of the gif in pixels
num_frames = 100  # number of frames in the animation

# gird variables
origin = (128, 128)
grid_w = 256
grid_h = 256
center = grid_w / 2
grid_x_units = 8
grid_y_units = 8

# circle variables
circle_w = 256  #
circle_h = 256  #
circle_x = 0    #
circle_y = 0    #

# dot variables
box_size = 12  
box_amp = 32
box_step = 0
box_inc = 0
box_x = 0
box_y = 0 
box_w = 32
box_h = 16
count = 1   
step = 1
amp = 1

# draws a new frame in the animation
def new_page(): 
    newPage(canvas, canvas) # new page from canvas variable
    frameDuration(1/24) # set the dividend to desired FPS (frames per second) 
    fill(0.1) # color of background
    rect(0, 0, canvas, canvas) # draw the background
    
# draws a circle from 5 arguments, see 'gird variables' above
def draw_box(box_w, box_h, box_x, box_y, box_amp, box_inc):  
    box_step = 0
    for box in range(64):
        
        box_x = math.cos(box) * box_amp
        box_y = -1 * math.sin(box) * box_amp
        fill(1, 1, 0)
        stroke(1, 1, 1)
        rect(box_x + center, box_y + center, box_size, box_size)
        box_step += box_inc * math.pi
        
# draws a grid from 5 arguments, see 'gird variables' above
def draw_grid(origin, width, height, num_x_units, num_y_units):
    unit_y = (height / num_y_units)
    unit_x = (width / num_x_units)
    translate(*origin)
    strokeWidth(1)
    stroke(0.5) 
    fill(None)
    step_x = 0 
    step_y = 0 
    
    for x in range(num_x_units + 1):
        line((step_x, 0), (step_x, height))
        step_x += unit_x
        
    for y in range(num_y_units + 1):
        line((0, step_y), (width, step_y))
        step_y += unit_y
    
    stroke(1, 0, 0)    
    rect(origin, origin, width, height)
                        
# draw each frame as a new page
for frame in range(num_frames):
    new_page()
    
    draw_grid(origin, grid_w, grid_h, grid_x_units, grid_y_units)
    
    box_amp = 32
    box_inc = 0.25
    draw_box(box_w, box_h, box_x, box_y, box_amp, box_inc)
    
saveImage("dbe_2016_03_16_v1.gif")