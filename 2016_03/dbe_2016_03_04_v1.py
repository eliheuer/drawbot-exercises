#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#  
#                                                                             #
#  Eli Heuer's daily DrawBot exercise                                         #
#                                                                             #
#  WWW: https://www.tumblr.com/blog/drawbot-exercises                         #
#  Mail: eliheuer@gmail.com                                                   #
#  Drawn on: 03/04/16 -- version 1                                            #
#  Made with DrawBot: http://www.drawbot.com/                                 #
#                                                                             #
#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#

import math # for cos and sin functions
    
# draws a new frame in the animation
def new_page(): 
    newPage(canvas, canvas)
    frameDuration(1/20)
    fill(0.8)
    rect(0, 0, canvas, canvas) 
    
# draws the red dot from to position variables    
def red_dot(x_pos, y_pos):
    fill(1, 0, 0)
    stroke(None)
    oval(int(x_pos) + center, int(y_pos) + center, circle_size, circle_size)
    
# draws a grid from a given increment 
def grid(increment):    
    fill(None)
    stroke(0.5)
    strokeWidth(1) 
   
    # draw the grid X-axis
    step_x  = -increment               
    for x in range(17):
        step_x = step_x + increment
        polygon((margin + step_x, margin), 
        (margin+step_x, canvas-margin))
    
    # draw the grid Y-axis
    step_y  = -increment  
    for y in range(17):
        step_y = step_y + increment
        polygon((margin, margin + step_y), 
        (canvas-margin, margin+step_y))
        
# setting variables
canvas = 512  # size of the gif in pixels
margin = 128  # grid distance from edge of canvas 
increment = 16  # grid increment
num_frames = 180  # number of frames in the animation
circle_size = 12  # self explanatory
center = int(canvas / 2) - 6 # exact center of the image
amp = 128 # short for amplitude
step = 0 # step in the animation

# draw each frame as a new page
for frame in range(num_frames):
    new_page() 
    grid(increment) 
    x_pos = math.cos(step) * amp
    y_pos = -1 * math.sin(step) * amp
    red_dot(x_pos, y_pos)
    step += 0.175
    step %= 8 * math.pi
    
saveImage("dbe_2016_03_04_v1.gif")