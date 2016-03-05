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
    
# draws a new frame in the animation
def new_page(): 
    newPage(canvas, canvas) # new page from canvas variable
    frameDuration(1/24) # set the dividend to desired FPS (frames per second) 
    fill(0.8) #light grey
    rect(0, 0, canvas, canvas) # background
        
def grid(origin, width, height, 
         num_horizontal_divisions, num_vertical_divisions):
    fill(None)
    stroke(0.5) # color
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
                     
        

# # draws a grid from a given increment 
# def grid(increment, canvas, margin):    
#     fill(None)
#     stroke(0.5)
#     strokeWidth(1) 
   
#     # draw the grid X-axis
#     step_x  = -increment               
#     for x in range(17):
#         step_x = step_x + increment
#         line((margin + step_x, margin), 
#             (margin+step_x, canvas-margin))
    
#     # draw the grid Y-axis
#     step_y  = -increment  
#     for y in range(17):
#         step_y = step_y + increment
#         line((margin, margin + step_y), 
#             (canvas-margin, margin+step_y))
        
# setting variables
canvas = 512  # size of the gif in pixels
margin = 128  # grid distance from edge of canvas 
increment = 16  # grid increment
num_frames = 32  # number of frames in the animation
circle_size = 12  # self explanatory
center = int(canvas / 2) - 6 # exact center of the image
amp = 128 # short for amplitude
step = 0 # step in the animation
origin = (32, 64)
width = 256
height = 256
num_horizontal_divisions = 16
num_vertical_divisions = 32

# draw each frame as a new page
for frame in range(num_frames):
    new_page()
    grid(origin, width, height, 
         num_horizontal_divisions, num_vertical_divisions)
    num_horizontal_divisions += 1
    width +=8
    
    
    
saveImage("dbe_2016_03_05_v1.gif")