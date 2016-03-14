#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#  
#                                                                             #
#  Eli Heuer's daily DrawBot exercise!                                        #
#                                                                             #
#  WWW: https://www.tumblr.com/blog/drawbot-exercises                         #
#  Mail: eliheuer@gmail.com                                                   #
#  Drawn on: 03/12/16 -- version 1                                            #
#  Made with DrawBot: http://www.drawbot.com/                                 #
#                                                                             #
#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#

# from drawBot import * # uncomment if using setupAsModule.py
import math # for cos and sin functions

# static variables
canvas = 512  # size of the gif in pixels
num_frames = 64  # number of frames in the animation

# gird variables
origin = (128, 128)
width = 256
height = 256
center = width/2
num_x_units = 8
num_y_units = 8

# red dot variables
dot_size = 32  
amp = 80 # short for amplitude
step = 0 # step in the animation
x_pos = 0 # x-axis position
y_pos = 0 # y-axis position
r = 0.2
g = 0.2
b = 0.2
r_array = range(-1600, 10000, 16)
g_array = range(-1600, 10000, 16)
b_array = range(-1600, 10000, 16)
print "r_array: ", r_array
color_cycle = 0

# draws a new frame in the animation
def new_page(): 
    newPage(canvas, canvas) # new page from canvas variable
    frameDuration(1/20) # set the dividend to desired FPS (frames per second) 
    fill(0.1) # color of background
    rect(0, 0, canvas, canvas) # draw the background

# draws the red dot from two position variables    
def red_dot(x_pos, y_pos, r, b, g):
    fill(r, g, b)
    stroke(None)
    oval(int(x_pos) + center, int(y_pos) + center, dot_size, dot_size)
       
# draws a grid from given arguments    
def grid(origin, width, height, num_x_units, num_y_units):
    translate(*origin)
    strokeWidth(1)
    stroke(0.7) 
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
    
    # animated dot
    for sub_frame in range(num_frames*8):
        r = r_array[sub_frame] * 0.0001
        g = g_array[sub_frame] * 0.0001
        b = g_array[sub_frame] * 0.0001
        color_cycle += 1
        x_pos = math.cos(step/2) * amp*2
        y_pos = -1 * math.sin(step) * amp/2

        red_dot((x_pos)-dot_size/2, (y_pos)-dot_size/2, r, g, b)
        step += 0.1001
        step %= 8 * math.pi
           
saveImage("dbe_2016_03_12_v1.gif")