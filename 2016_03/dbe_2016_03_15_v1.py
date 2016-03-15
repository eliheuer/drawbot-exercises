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
num_frames = 100  # number of frames in the animation

# gird variables
origin = (128, 128)
width = 256
height = 256
center = width/2
num_x_units = 8
num_y_units = 8

# circle variables
circle_w = 256  #
circle_h = 256  #
circle_x = 0    #
circle_y = 0    #
divisions = 8   
step = 0
amp = 0 

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
def draw_circle_old_news(width, height, x_pos, y_pos, divisions):
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
    
# draws a guide showing the sine of dot    
def draw_circle(circle_w, circle_h, circle_x, circle_y, divisions):
    
    for segment in range(divisions):
        # create a new empty path
        newPath()
        stroke(3)
        fill(1, 0, 0)
        # set the first oncurve point
        moveTo((128, 128))
        # line to from the previous point to a new point
        lineTo((100, 200))
        lineTo((200, 200))
        # curve to a point with two given handles
        lineTo((128,128))
        # close the path
        closePath()
        # draw the path
        drawPath()
        
def draw_type():
    fontSize(24)
    font("Helvetica Neue Bold")
    tracking(0)
    fill(1, 1, 1)
    stroke(None)
    text("Happy Hardcore", (-2, -32))

def anime():
        # animated dot
    x_pos = math.cos(step) * amp
    y_pos = -1 * math.sin(step) * amp
    x_pos_string = "{:.3f}".format(x_pos)
    y_pos_string = "{:.3f}".format(y_pos)
    print "x position: ", x_pos_string
    print "y position: ", y_pos_string
    
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
    draw_grid(origin, width, height, num_x_units, num_y_units)

    draw_circle(circle_w, circle_h, circle_x, circle_y, divisions)
    
    draw_type()

    step += 0.02 * math.pi
               
saveImage("dbe_2016_03_15_v2.gif")