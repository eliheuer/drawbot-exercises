#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#  
#                                                                             #
#  Eli Heuer's daily DrawBot exercise!                                        #
#                                                                             #
#  WWW: https://www.tumblr.com/blog/drawbot-exercises                         #
#  Mail: eliheuer@gmail.com                                                   #
#  Drawn on: Pi Day! 03/14/16 -- version 2                                    #
#  Made with DrawBot: http://www.drawbot.com/                                 #
#                                                                             #
#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#

# from drawBot import * # uncomment if using setupAsModule.py
import math # for cos, sin and pi functions

# static variables
canvas = 512  # size of the gif in pixels
num_frames = 100  # number of frames in the animation

# gird variables
origin = (128, 128)
width = 256
height = 256
center = width/2
num_x_units = 8
num_y_units = 8

# dot variables
dot_size = 16  
amp = 128 # short for amplitude
step = 0 # step in the animation
fake_step = math.pi # a dumb hack >_<
step_string = "{:.8f}".format(fake_step)
x_pos = 0 # x-axis position
y_pos = 0 # y-axis position
r = 1
g = 1
b = 1

# draws a new frame in the animation
def new_page(): 
    newPage(canvas, canvas) # new page from canvas variable
    frameDuration(1/24) # set the dividend to desired FPS (frames per second) 
    fill(0.1) # color of background
    rect(0, 0, canvas, canvas) # draw the background

# draws the dot from two position variables    
def dot(x_pos, y_pos, r, b, g):
    fill(1, 0, 0)
    stroke(None)
    oval(int(x_pos) + center, int(y_pos) + center, dot_size, dot_size)
    
# draws a guide showing the sine of dot    
def sine_lines(width, height, x_pos, y_pos, r, b, g):
    fill(r, g, b)
    stroke(None)
    oval(center-dot_size/2, center-dot_size/2, dot_size, dot_size)
    oval(int(x_pos) + center, center-dot_size/2, dot_size, dot_size)
    fill(None)
    strokeWidth(3)
    stroke(r, g, b)
    line((center, center), 
        (int(x_pos) + (center+dot_size/2), int(y_pos) + (center+dot_size/2)))
    line((center, center), 
        (int(x_pos) + (center+dot_size/2), center))
    line((int(x_pos) + (center+dot_size/2), center), 
        (int(x_pos) + (center+dot_size/2), int(y_pos) + (center+dot_size/2)))
    oval(center-128, center-128, width, height)
       
# draws a grid from given arguments    
def grid(origin, width, height, num_x_units, num_y_units):
    translate(*origin)
    strokeWidth(1)
    stroke(0.5) 
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
    x_pos = math.cos(step) * amp
    y_pos = -1 * math.sin(step) * amp
    x_pos_string = "{:.3f}".format(x_pos)
    y_pos_string = "{:.3f}".format(y_pos)
    print "x position: ", x_pos_string
    print "y position: ", y_pos_string
    
    sine_lines(width, height, (x_pos)-dot_size/2, (y_pos)-dot_size/2, r, g, b)
    dot((x_pos)-dot_size/2, (y_pos)-dot_size/2, r, g, b)
    
    # type 
    fontSize(24)
    font("Helvetica Neue Bold")
    tracking(0)
    fill(1, 1, 1)
    stroke(None)
    text("Happy π Day", (-2, -32))
    fill(1, 0, 0)
    text(step_string, (-2, -64))
    
    step += 0.02 * math.pi
    step_string = "{:.8f}".format(fake_step)
    fake_step -= math.pi / 100
               
saveImage("dbe_2016_03_14_v2.gif")