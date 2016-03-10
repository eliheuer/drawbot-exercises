#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#  
#                                                                             #
#  Eli Heuer's daily DrawBot exercise!                                        #
#                                                                             #
#  WWW: https://www.tumblr.com/blog/drawbot-exercises                         #
#  Mail: eliheuer@gmail.com                                                   #
#  Drawn on: 03/10/16 -- version 1                                            #
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
    frameDuration(1/4) # set the dividend to desired FPS (frames per second) 
    fill(0.7, 0.7, 0.7) #dark grey
    rect(0, 0, canvas, canvas) # background

# draws a grid from given arguments    
def grid(origin, width, height, num_x_divisions, num_y_divisions):
    fill(None)
    stroke(0.1, 0.1, 0.1) # color
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
    

    translate(0, 256)
    stroke(0.1, 0.1, 0.1)
    
    if frame >= 1:
        fill(0.9, 0.2, 0.2)
        rotate(-90)
        translate(64, 64)
        polygon((0, 0), (32, 32), (0, 64), close=True)
        
    if frame >= 2:
        fill(0.9, 0.5, 0.2)    
        rotate(180)
        translate(-32, -96)
        polygon((0, 0), (32, 32), (0, 64), close=True)
    
    if frame >= 3:
        fill(0.9, 0.9, 0.2)       
        rotate(180)
        translate(-32, -32)
        polygon((0, 0), (32, 32), (0, 64), close=True)

    if frame >= 4:
        fill(0.5, 0.9, 0.2)    
        rotate(-90)
        translate(-64, 0)
        polygon((0, 0), (32, 32), (0, 64), close=True)

    if frame >= 5:
        fill(0.2, 0.9, 0.2)
        rotate(180)
        translate(-32, -96)
        polygon((0, 0), (32, 32), (0, 64), close=True)

    if frame >= 6:
        fill(0.2, 0.9, 0.5)
        rotate(180)
        translate(-32, -32)
        polygon((0, 0), (32, 32), (0, 64), close=True)

    if frame >= 7:
        fill(0.2, 0.9, 0.9)
        rotate(-90)
        translate(-64, 0)
        polygon((0, 0), (32, 32), (0, 64), close=True)

    if frame >= 8:
        fill(0.2, 0.5, 0.9)
        rotate(180)
        translate(-32, -96)
        polygon((0, 0), (32, 32), (0, 64), close=True)

    if frame >= 9:
        fill(0.2, 0.2, 0.9)
        rotate(180)
        translate(-32, -32)
        polygon((0, 0), (32, 32), (0, 64), close=True)

    if frame >= 10:
        fill(0.5, 0.2, 0.9)
        rotate(-90)
        translate(-64, 0)
        polygon((0, 0), (32, 32), (0, 64), close=True)

    if frame >= 11:
        fill(0.9, 0.2, 0.9)
        rotate(180)
        translate(-32, -96)
        polygon((0, 0), (32, 32), (0, 64), close=True)

    if frame >= 12:
        fill(0.9, 0.2, 0.5)
        rotate(180)
        translate(-32, -32)
        polygon((0, 0), (32, 32), (0, 64), close=True)     
           
saveImage("dbe_2016_03_10_v1.gif")