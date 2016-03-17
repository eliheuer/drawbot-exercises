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

# static variables
canvas = 512 
num_frames = 76 

# gird variables
origin = (128, 128)
width = 256
height = 256
center = width/2
num_x_units = 7
num_y_units = 7

# circle variables
circle_w = 256 - 32
circle_h = 256 - 32
circle_x = 0
circle_y = 0
divisions = 0

# box variables
box_size_x = 36 * 2
box_size_y = 36
box_amp = 110
box_step = 0
box_inc = 16
x_pos = 0
y_pos = 0
box_color = 1
box_count = 100
box_start = 0
box_start_step = 0

# draws a new frame in the animation
def new_page(): 
    newPage(canvas, canvas) 
    frameDuration(1/20) 
    fill(0.8) 
    rect(0, 0, canvas, canvas) 

# draws the dot from two position variables    
def box(x_pos, y_pos, box_size_x, box_size_y, box_color):
    fill((x_pos * 0.02) + 1, (y_pos * -0.01) + 1, 0.5)
    strokeWidth(1)
    stroke(0.1)
    rect(int(x_pos) + center, int(y_pos) + center, 
        box_size_x, box_size_y)
    
# draws a circle from 5 arguments, see 'gird variables' above
def draw_circle(circle_w, circle_h, circle_x, circle_y, 
    box_count, dot_amp, box_step, dot_inc, box_start):
   
    for segment in range(box_count):
        box_x = math.cos(box_step + box_start) * (box_amp - 16)
        box_y = -1 * math.sin(box_step + box_start) * box_amp
        box((box_x)-box_size_x/2, (box_y)-box_size_y/2, 
            box_size_x, box_size_y, box_color)
        
        box_step += 0.02 * math.pi
       
# draws a grid from given arguments    
def grid(origin, width, height, num_x_units, num_y_units):
    translate(*origin)
    strokeWidth(2)
    stroke(1) 
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
    draw_circle(circle_w, circle_h, circle_x, circle_y, 
        box_count, box_amp, box_step, box_inc, box_start)
    box_count_string = "{:03d}".format(box_count)
    box_count += 1
    box_start += 0.02 

saveImage("dbe_2016_03_17_v1.gif")