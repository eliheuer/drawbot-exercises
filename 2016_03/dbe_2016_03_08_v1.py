#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#  
#                                                                             #
#  Eli Heuer's daily DrawBot exercise!                                        #
#                                                                             #
#  WWW: https://www.tumblr.com/blog/drawbot-exercises                         #
#  Mail: eliheuer@gmail.com                                                   #
#  Drawn on: 03/08/16 -- version 1                                            #
#  Made with DrawBot: http://www.drawbot.com/                                 #
#                                                                             #
#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#

import math # for cos and sin functions

# static variables
canvas = 512  # size of the gif in pixels
num_frames = 16  # number of frames in the animation
center = 128 # exact center of the image

# gird variables
origin = (128, 128)
width = 256
height = 256
num_x_divisions = 1
num_y_divisions = 1

# red dot variables
circle_size = 256
amp = 64 # short for amplitude
step = 0 # step in the animation
x_pos = 0 # x-axis position
y_pos = 0 # y-axis position

# draws a new frame in the animation
def new_page(): 
    newPage(canvas, canvas) # new page from canvas variable
    frameDuration(1/1) # set the dividend to desired FPS (frames per second) 
    fill(0.0, 0.0, 0.1) #dark grey
    rect(0, 0, canvas, canvas) # background
    
# draws the red dot from to position variables    
def red_dot(x_pos, y_pos, circle_size):
    fill(1, 0, 0)
    stroke(None)
    oval(int(x_pos), int(y_pos), circle_size, circle_size)
    
# draws a grid from given arguments    
def grid(origin, width, height, num_x_divisions, num_y_divisions):
    fill(None)
    stroke(1, 0, 0) # color
    strokeWidth(1)
    
    translate(*origin)
    step_x = 0 
    increment_x = width / num_x_divisions
    for x in range(num_x_divisions + 1):
        line((step_x, 0), (step_x, height))
        step_x += increment_x
        
    step_y = 0 
    increment_y = height / num_y_divisions
    for y in range(num_y_divisions + 1):
        line((0, step_y), (width, step_y))
        step_y += increment_y

# draw each frame as a new page
for frame in range(8):
    new_page()    
    step =+ 1
    # draw the grid
    grid(origin, width, height, num_x_divisions, num_y_divisions)
    num_x_divisions += 1
    num_y_divisions += 1
    # animated  dot 
    red_dot(x_pos, y_pos, circle_size)
    circle_size = width / num_x_divisions
    
for frame in range(8):
    new_page()    
    step =+ 1
    # draw the grid
    grid(origin, width, height, num_x_divisions, num_y_divisions)
    num_x_divisions -= 1
    num_y_divisions -= 1
    # animated  dot 
    red_dot(x_pos, y_pos, circle_size)
    circle_size = width / num_x_divisions
         
saveImage("dbe_2016_03_08_v1.gif")