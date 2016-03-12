#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#  
#                                                                             #
#  Eli Heuer's daily DrawBot exercise!                                        #
#                                                                             #
#  WWW: https://www.tumblr.com/blog/drawbot-exercises                         #
#  Mail: eliheuer@gmail.com                                                   #
#  Drawn on: 03/11/16 -- version 1                                            #
#  Made with DrawBot: http://www.drawbot.com/                                 #
#                                                                             #
#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#

import math # for cos and sin functions

# static variables
canvas = 512  # size of the gif in pixels
num_frames = 323  # number of frames in the animation
center = 128

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
spacing = 0


ball_size_x =[40, 36, 34, 32, 32, 30, 30, 30, 30, 32, 32, 32, 32, 32, 32, 32,
    32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32]
print "ball_size_x: ", len(ball_size_x)

ball_size_y =[32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32,
    32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32]
print "ball_size_y: ", len(ball_size_y)

ball_pos_x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print "ball_pos_x: ", len(ball_pos_x)

ball_pos_y = [0, 4, 8, 32, 48, 64, 80, 96, 128, 144, 160, 196, 210, 218, 220, 224, 224, 220, 218, 210, 196, 160, 144, 128, 112, 96, 80, 64, 48, 32, 16, 2]
print "ball_pos_y: ", len(ball_pos_y)
    
print range(512, 0, -16)

# draws a new frame in the animation
def new_page(): 
    newPage(canvas, canvas) # new page from canvas variable
    frameDuration(1/20) # set the dividend to desired FPS (frames per second) 
    fill(0.1) #dark grey
    rect(0, 0, canvas, canvas) # background
    
# draws a grid from given arguments    
def grid(origin, width, height, num_x_divisions, num_y_divisions):
    fill(None)
    stroke(0.5) # color
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
    spacing += 0.28
    fontSize(32)
    font("Helvetica Neue Bold")
    tracking(-1.2)
    fill(0.5)
    stroke(None)
    text("Hello World", (-2, -32))
    
    # animated  dot
    fill(0.9, 0.1, 0.1)
    stroke(None)
    oval(ball_pos_x[step], ball_pos_y[step], ball_size_x[step], ball_size_y[step])
    step += 1

    
saveImage("dbe_2016_03_11_v1.gif")