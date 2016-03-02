#  Eli Heuer's daily DrawBot exercise!
#  eliheuer@gmail.com
#  03/01/16 -- version 1
#  Made with DrawBot:
#  http://www.drawbot.com/ 

#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#

import math
print "start"
def dot(x_pos, y_pos):
    x=math.cos(math.radians(y_pos*64))
    
    print x
    fill(1)
    stroke(1, 0, 0)
    strokeWidth(2)
    oval(x_pos, x*64, circle_size, circle_size)

def grid():    
    # style the grid
    fill(None)
    stroke(0.5)
    strokeWidth(1)
    lineCap("round")
    lineJoin("round")   
    # draw the grid X-axis
    stepx  = -16  # step in sequence on x axis             
    for x in range(17):
        save()
        stepx = stepx + increment
        polygon((margin + stepx, margin), (margin+stepx, canvas-margin))
        restore()
    # draw the grid Y-axis
    stepy  = -16  # step in sequence on y axis 
    for y in range(17):
        save()
        stepy = stepy + increment
        polygon((margin, margin + stepy), (canvas-margin, margin+stepy))
        restore()

canvas = 512  # size of the gif in pixels
margin = 128  # grids distance from edge of canvas 
increment = 16  # grid increment
num_frames = 17  # number of frames in the animation
step_h = 128  # horizontal steps in looping animation
step_v = 0  # vertical steps in looping animation
circle_size = 12  # self explanatory

# grid increments (16px X 16pc)
gridarray_reg = range(margin, (canvas - margin) + increment, increment) 
gridarray_rev = gridarray_reg[::-1]

# draw each frame as a new page
for frame in range(num_frames):
    newPage(canvas, canvas)
    step_h = step_h + 1
    frameDuration(1/20)
    fill(0.8)
    rect(0, 0, canvas, canvas)  
    grid()    
    step_v = step_v + 1
    translate(0, 256)
    dot(step_h, step_v)
print "end"
saveImage("dbe_2016_02_29_v1.gif")