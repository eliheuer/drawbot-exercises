#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#  
#                                                                             #
#  Eli Heuer's daily DrawBot exercise                                         #
#                                                                             #
#  WWW: https://www.tumblr.com/blog/drawbot-exercises                         #
#  Mail: eliheuer@gmail.com                                                   #
#  Drawn on: 03/05/16 -- version 1                                            #
#  Made with DrawBot: http://www.drawbot.com/                                 #
#                                                                             #
#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#

import math # for cos and sin functions
# main variables
canvas = 512  # size of the gif in pixels
num_frames = 64  # number of frames in the animation
center = int(canvas / 2) # exact center of the image

# gird variables
origin = (128, 128)
width = 256
height = 256
num_horizontal_divisions = 1
num_vertical_divisions = 1

# draws a new frame in the animation
def new_page(): 
    newPage(canvas, canvas) # new page from canvas variable
    frameDuration(1/20) # set the dividend to desired FPS (frames per second) 
    fill(0.1) #dark grey
    rect(0, 0, canvas, canvas) # background
 
# draws a grid from given arguments    
def grid(origin, width, height, 
         num_horizontal_divisions, num_vertical_divisions):
    fill(None)
    stroke(0.9) # color
    strokeWidth(1)
    
    translate(*origin)
    step_x = 0 
    increment_x = width / num_horizontal_divisions
    for x in range(num_horizontal_divisions + 1):
        line((step_x, 0), (step_x, height))
        step_x += increment_x
        
    step_y = 0 
    increment_y = height / num_vertical_divisions
    for y in range(num_vertical_divisions + 1):
        line((0, step_y), (width, step_y))
        step_y += increment_y

# draw each frame as a new page
for frame in range(int(num_frames/2)):
    new_page()
    grid(origin, width, height, 
        num_horizontal_divisions, num_vertical_divisions)
    
    fontSize(32)
    font("Lydian")
    tracking(0)
    fill(0.9)
    stroke(None)
    text("Hello World", (-2, -frame))
    
for frame in range(int(num_frames/2)):
    new_page()
    grid(origin, width, height, 
        num_horizontal_divisions, num_vertical_divisions)
    num_horizontal_divisions += 1
    num_vertical_divisions += 1
    
    # type -- future idea: print out variable data?
    fontSize(32)
    font("Lydian")
    tracking(0)
    fill(0.9)
    stroke(None)
    text("Hello World", (-2, -32))

saveImage("dbe_2016_03_05_v1.gif")