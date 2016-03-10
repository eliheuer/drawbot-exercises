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

# setting variables
canvas = 512  # size of the gif in pixels
num_frames = 32  # number of frames in the animation
bar_size = 12  
center = int(canvas / 2) - 6 # exact center of the image
spacing = 0
step = 0
amp = 0
red_bar_x_pos = -256 + 6
red_bar_y_pos = -256 + 6
bar_range_up = range(0, 264, 8)
bar_range_down = range(248, -8, -8)
bar_range = bar_range_up + bar_range_down 
print bar_range

# gird variables
origin = (128, 128)
width = 256
height = 256
num_x_divisions = 8
num_y_divisions = 8

# draws a new frame in the animation
def new_page(): 
    newPage(canvas, canvas) # new page from canvas variable
    frameDuration(1/24) # set the dividend to desired FPS (frames per second) 
    fill(0.7, 0.7, 0.7) #dark grey
    rect(0, 0, canvas, canvas) # background

# draws a grid from given arguments    
def grid(origin, width, height, num_x_divisions, num_y_divisions):
    fill(None)
    stroke(0.3) # color
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
    
# draws the red dot from to position variables    
def red_bar(red_bar_x_pos, red_bar_y_pos, red_bar_x_size, red_bar_y_size):
    fill(1, 0, 0)
    stroke(None)
    rect(int(red_bar_x_pos) + center, int(red_bar_y_pos) + center, 32, red_bar_y_size)
    
# draw each frame as a new page
for frame in range(num_frames):
    new_page() 
    bar_size = width / num_x_divisions
    
    # draw the grid
    grid(origin, width, height, num_x_divisions, num_y_divisions)
    
    # type -- future idea: print out variable data?
    spacing += 0.28
    fontSize(32)
    font("Helvetica Neue Bold")
    tracking(-1.2)
    fill(0.3)
    stroke(None)
    text("Hello World", (-2, -32))
    
    red_bar_x_size = math.cos(step) * amp
    red_bar_x_size = red_bar_x_size + 128
    red_bar_y_size = math.sin(step) * amp
    print "red_bar_x_size: ", red_bar_x_pos
    print "red_bar_y_size: ", red_bar_y_pos
    print " "
    red_bar(red_bar_x_pos, red_bar_y_pos, red_bar_x_size, red_bar_y_size)
    step += 0.175
    step %= 8 * math.pi
    
    
saveImage("dbe_2016_03_10_v1.gif")