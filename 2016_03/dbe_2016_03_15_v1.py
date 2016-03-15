#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#  
#                                                                             #
#  Eli Heuer's daily DrawBot exercise!                                        #
#                                                                             #
#  WWW: https://www.tumblr.com/blog/drawbot-exercises                         #
#  Mail: eliheuer@gmail.com                                                   #
#  Drawn on: 03/15/16 -- version 2                                            #
#  Made with DrawBot: http://www.drawbot.com/                                 #
#                                                                             #
#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#

# from drawBot import * # uncomment if using setupAsModule.py
import math # for cos, sin and pi functions

# static variables
canvas = 512  # size of the gif in pixels
num_frames = 50  # number of frames in the animation

# gird variables
origin = (128, 128)
grid_w = 256
grid_h = 256
center = grid_w / 2
grid_x_units = 8
grid_y_units = 8

# circle variables
circle_w = 256  #
circle_h = 256  #
circle_x = 0    #
circle_y = 0    #
divisions = 0   
step = 0
amp = 0

# dot variables
dot_size = 16  
dot_amp = 64 # short for amplitude
dot_step = 0.0 # step in the animation
dot_x = 0 # x-axis position
dot_y = 0 # y-axis position

# draws a new frame in the animation
def new_page(): 
    newPage(canvas, canvas) # new page from canvas variable
    frameDuration(1/24) # set the dividend to desired FPS (frames per second) 
    fill(0.1) # color of background
    rect(0, 0, canvas, canvas) # draw the background


# draws the dot from two position variables    
def dot(dot_x, dot_y):
    fill(1, 0, 0)
    stroke(None)
    oval(int(dot_x) + center, int(dot_y) + center, dot_size, dot_size)
    
# draws a circle from 5 arguments, see 'gird variables' above
def draw_circle(circle_w, circle_h, circle_x, circle_y, divisions, dot_step):
    # dot        
    for segment in range(divisions):
        
        oval(112, 112, 16, 16)
        
        dot_x = math.cos(dot_step) * dot_amp
        dot_y = -1 * math.sin(dot_step) * dot_amp
        x_pos_string = "{:.3f}".format(dot_x)
        y_pos_string = "{:.3f}".format(dot_y)
        print "x position: ", x_pos_string
        print "y position: ", y_pos_string
    
        dot((dot_x)-dot_size/2, (dot_y)-dot_size/2)
    
        dot_step += 0.04 * math.pi
        
        # create a new empty path
        newPath()
        stroke(3)
        fill(1, 0, 0)
        # set the first oncurve point
        moveTo((128, 128))
        # line to from the previous point to a new point
        lineTo((100, 200))
        lineTo((150, 250))
        lineTo((200, 200))
        # curve to a point with two given handles
        lineTo((128,128))
        # close the path
        closePath()
        # draw the path
        drawPath()
        
def draw_type():
    fontSize(30)
    font("Helvetica Neue Bold")
    tracking(0)
    fill(1, 1, 1)
    stroke(None)
    text("Techno Subgenre:", (-2, -32))
    fill(1, 1, 0)
    text("Happy Hardcore", (-2, -64))
    
# draws a grid from 5 arguments, see 'gird variables' above
def draw_grid(origin, width, height, num_x_units, num_y_units):
    unit_y = (height / num_y_units)
    unit_x = (width / num_x_units)
    translate(*origin)
    strokeWidth(1)
    stroke(0.5) 
    fill(None)
    step_x = 0 
    step_y = 0 
    
    for x in range(num_x_units + 1):
        line((step_x, 0), (step_x, height))
        step_x += unit_x
        
    for y in range(num_y_units + 1):
        line((0, step_y), (width, step_y))
        step_y += unit_y
                
# draw each frame as a new page
for frame in range(num_frames):
    new_page()
    
    draw_grid(origin, grid_w, grid_h, grid_x_units, grid_y_units)
    
    fill(1, 1, 0)
    oval(32, 32, 192, 192)
    
    draw_circle(circle_w, circle_h, circle_x, circle_y, divisions, dot_step)
    draw_type()
    
    divisions += 1
               
saveImage("dbe_2016_03_15_v2.gif")