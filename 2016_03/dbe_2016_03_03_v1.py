#  Eli Heuer's daily DrawBot exercise!
#  eliheuer@gmail.com
#  03/03/16 -- version 1
#  Made with DrawBot:
#  http://www.drawbot.com/ 

#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#

import math

def sin_dot(frame):
    translate(0, 256)
    y = math.sin(math.radians(frame*8))
    y = y * 128
    y = round(y)
    y = int(y)
    print (y)
    fill(1, 0, 0)
    stroke (None)
    translate(256, 0)
    oval(y-6, y-6, circle_size, circle_size)
    
# set up a new frame in the animation
def new_page():
    newPage(canvas, canvas)
    frameDuration(1/20)
    fill(0.8)
    rect(0, 0, canvas, canvas) 
    
# draw a grid 
def grid(increment):    
    fill(None)
    stroke(0.5)
    strokeWidth(1)
    lineCap("round")
    lineJoin("round")   
   
    # draw the grid X-axis
    stepx  = -increment               
    for x in range(17):
        save()
        stepx = stepx + increment
        polygon((margin + stepx, margin), 
        (margin+stepx, canvas-margin))
        restore()
    
    # draw the grid Y-axis
    stepy  = -increment  
    for y in range(17):
        stepy = stepy + increment
        polygon((margin, margin + stepy), 
        (canvas-margin, margin+stepy))
        
# setting global variables
canvas = 512  # size of the gif in pixels
margin = 128  # grids distance from edge of canvas 
increment = 16  # grid increment
num_frames = 90  # number of frames in the animation
circle_size = 12  # self explanatory



# draw each frame as a new page
print "start"
for frame in range(num_frames):
    grid_array_reg = range(margin, (canvas - margin) + increment, increment) 
    grid_array_rev = grid_array_reg[::-1]
    new_page() 
    grid(increment)  
    for step in range(16):
        save()
        sin_dot(frame)
        restore()
    
print "end" 
saveImage("dbe_2016_03_03_v1.gif")