#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#  
#                                                                             #
#  Eli Heuer's daily DrawBot exercise!                                        #
#                                                                             #
#  WWW: https://www.tumblr.com/blog/drawbot-exercises                         #
#  Mail: eliheuer@gmail.com                                                   #
#  Drawn on: 03/09/16 -- version 1                                            #
#  Made with DrawBot: http://www.drawbot.com/                                 #
#                                                                             #
#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#

import math # for cos and sin functions
import random

# static variables
canvas = 512  # size of the gif in pixels
num_frames = 16  # number of frames in the animation
center = 128 # exact center of the image

# gird variables
origin = (128, 128)
width = 256
height = 256
num_x_divisions = 16
num_y_divisions = 16

x_pos = 128+64
y_pos = 128-32
wedge_color_r = 1
wedge_color_g = 1
wedge_color_b = 0


# draws a new frame in the animation
def new_page(): 
    newPage(canvas, canvas) # new page from canvas variable
    frameDuration(1/1) # set the dividend to desired FPS (frames per second) 
    fill(0.0, 0.0, 0.1) #dark grey
    rect(0, 0, canvas, canvas) # background
    
def quarter_wedge(x_pos, y_pos, wedge_color_r, wedge_color_g, wedge_color_b):
    fill(wedge_color_r, wedge_color_g, wedge_color_b)
    stroke(None) # color
    # create a bezier path
    path = BezierPath()

    # move to a point
    path.moveTo((x_pos, y_pos))
    # line to a point
    path.lineTo((x_pos+0, y_pos+64))
    path.lineTo((x_pos+32, y_pos+32))
    # close the path
    path.closePath()
    drawPath(path)

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
for frame in range(num_frames):
    new_page()    
    # draw the grid
    grid(origin, width, height, num_x_divisions, num_y_divisions)
    # wedge
    
    # one
    quarter_wedge(x_pos, y_pos, wedge_color_r, wedge_color_g, wedge_color_b)
    



            
saveImage("dbe_2016_03_08_v1.gif")