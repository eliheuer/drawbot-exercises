#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#  
#                                                                             #
#  Eli Heuer's daily DrawBot exercise!                                        #
#                                                                             #
#  WWW: https://www.tumblr.com/blog/drawbot-exercises                         #
#  Mail: eliheuer@gmail.com                                                   #
#  Drawn on: 03/15/16 -- version 1                                           #
#  Made with DrawBot: http://www.drawbot.com/                                 #
#                                                                             #
#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#

# from drawBot import * # uncomment if using setupAsModule.py
import math # for cos, sin and pi functions

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
dot_size = 12  
dot_amp = 32
amp_step = 0
dot_step = 0.0
dot_inc = 0.04
dot_x = 0
dot_y = 0 
divisions = 1   
step = 1
amp = 1
r = 1
g = 1
b = 0

# draws a new frame in the animation
def new_page(): 
    newPage(canvas, canvas) # new page from canvas variable
    frameDuration(1/24) # set the dividend to desired FPS (frames per second) 
    fill(0.1) # color of background
    rect(0, 0, canvas, canvas) # draw the background
    
# draws the dot from two position variables    
def dot(dot_x, dot_y, r, g, b):
    fill(r, g, b)
    stroke(None)
    oval(int(dot_x) + center, int(dot_y) + center, dot_size, dot_size)
    
# draws a circle from 5 arguments, see 'gird variables' above
def draw_circle(circle_w, circle_h, circle_x, circle_y, 
    divisions, dot_amp, dot_step, dot_inc, r, g, b):
    # dot        
    for segment in range(divisions):
        
        dot_x = math.cos(dot_step) * dot_amp
        dot_y = -1 * math.sin(dot_step) * dot_amp
        dot((dot_x)-dot_size/2, (dot_y)-dot_size/2, r, g, b)
        dot_step += dot_inc * math.pi
        
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
                
# draw each frame as a new page
for frame in range(num_frames):
    new_page()

    draw_grid(origin, grid_w, grid_h, grid_x_units, grid_y_units)

    r = 1
    g = 0 
    b = 0
    dot_amp = 32 + amp_step
    dot_inc = 0.25
    draw_circle(circle_w, circle_h, circle_x, circle_y, 
        divisions, dot_amp, dot_step, dot_inc, r, g, b)
    
    r = 1
    g = 0.5 
    b = 0
    dot_amp = 64 + amp_step
    dot_inc = 0.125
    draw_circle(circle_w, circle_h, circle_x, circle_y, 
        divisions, dot_amp, dot_step, dot_inc, r, g, b)
     
    r = 1
    g = 1
    b = 0
    dot_amp = 96 + amp_step
    dot_inc = 0.0625
    draw_circle(circle_w, circle_h, circle_x, circle_y, 
        divisions, dot_amp, dot_step, dot_inc, r, g, b)
    
    amp_step += 1
    divisions += 1
               
saveImage("dbe_2016_03_15_v1.gif")