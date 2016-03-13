#  Eli Heuer's daily DrawBot exercise!
#  eliheuer@gmail.com
#  03/01/16 -- version 1
#  Made with DrawBot:
#  http://www.drawbot.com/ 

#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/

import math

def circle (x, y):
    oval((gridarray_reg[step_h])-(circle_size/2), 
    (gridarray_reg[step_v+move])-(circle_size/2), 
    circle_size, circle_size)   

def grid (x, y):
    
# setting up the main variables
canvas      =  512  # size of the gif in pixels
margin      =  128  # grids distance from edge of canvas 
increment   =   16  # grid increment
num_frames  =   17  # number of frames in the animation
step_h      =   -2  # horizontal steps in looping animation
step_v      =    0  # vertical steps in looping animation
circle_size =   12  # self explanatory

# grid increments (16px X 16pc)
gridarray_reg = range(margin, (canvas - margin) + increment, increment) 
gridarray_rev = gridarray_reg[::-1]

# draw the canvas
for frame in range(num_frames):
    newPage(canvas, canvas)
    step_h = step_h + 1
    frameDuration(1/20)
    fill(0.8)
    rect(0, 0, canvas, canvas)
  
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
    
    # animation loop
    for frame in range(num_frames):
        save()
        fill(1)
        strokeWidth(1.5)
        stroke(0.4)
    
    # moving circles
    if step_h <= 16:
        for move in range(17):
            step_h = step_h + 1
            if step_h <= 16:
                oval((gridarray_reg[step_h])-(circle_size/2), 
                (gridarray_reg[step_v+move])-(circle_size/2), 
                circle_size, circle_size)   
            else:
                step_h = 0
    else:
        step_h = 0 
        
    restore()
    
saveImage("dbe_2016_02_29_v1.gif")