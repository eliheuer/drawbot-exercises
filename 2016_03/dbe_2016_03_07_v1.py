#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#  
#                                                                             #
#  Eli Heuer's daily DrawBot exercise!                                        #
#                                                                             #
#  WWW: https://www.tumblr.com/blog/drawbot-exercises                         #
#  Mail: eliheuer@gmail.com                                                   #
#  Drawn on: 03/07/16 -- version 1                                            #
#  Made with DrawBot: http://www.drawbot.com/                                 #
#                                                                             #
#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#

import math # for cos and sin functions

# static variables
canvas = 512  # size of the gif in pixels
num_frames = 63  # number of frames in the animation
center = 128 # exact center of the image

# gird variables
origin = (128, 128)
width = 256
height = 256
num_x_divisions = 8
num_y_divisions = 8

# red dot variables
circle_size = 16  # self explanatory
amp = 64 # short for amplitude
step = 0 # step in the animation
x_pos = 0 # x-axis position
y_pos = 0 # y-axis position


# draws a new frame in the animation
def new_page(): 
    newPage(canvas, canvas) # new page from canvas variable
    frameDuration(1/20) # set the dividend to desired FPS (frames per second) 
    fill(0.1) #dark grey
    rect(0, 0, canvas, canvas) # background
    
# draws the red dot from to position variables    
def red_dot(x_pos, y_pos):
    fill(1, 0, 0)
    stroke(None)
    oval(int(x_pos) + center, int(y_pos) + center, circle_size, circle_size)
    
# draws the red dot from to position variables    
def yellow_dot(x_pos, y_pos):
    fill(1, 1, 0)
    stroke(None)
    oval(int(x_pos) + center, int(y_pos) + center, circle_size, circle_size)

# draws the red dot from to position variables    
def blue_dot(x_pos, y_pos):
    fill(0, 0, 1)
    stroke(None)
    oval(int(x_pos) + center, int(y_pos) + center, circle_size, circle_size)
 
# draws a grid from given arguments    
def grid(origin, width, height, num_x_divisions, num_y_divisions):
    fill(None)
    stroke(0.9) # color
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
for frame in range(int(num_frames)):
    new_page()
    
    # draw the grid
    grid(origin, width, height, num_x_divisions, num_y_divisions)
    
    # type -- future idea: print out variable data?
    fontSize(32)
    font("Helvetica Neue Bold")
    tracking(2)
    fill(0.9)
    stroke(None)
    text("Hello World", (-2, -32))
    
    # animated  dot
    for move in range(frame):
        x_pos = math.cos(step) * amp
        y_pos = -1 * math.sin(step) * amp
    
        red_dot((x_pos)-8, (y_pos)-8)
        yellow_dot(0-8, 0-8)
        blue_dot((x_pos*2)-8, (y_pos*2)-8)
    
        step += 0.1 
        step %= 8 * math.pi
    
saveImage("dbe_2016_03_07_v1.gif")