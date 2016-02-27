#  Eli Heuer's daily DrawBot exercise!
#  eliheuer@gmail.com
#  02/26/16 -- version 1
#  Made with DrawBot:
#  http://www.drawbot.com/ 

# pep-8 maximum-line-length #/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#

# setting up the canvas size and main variables

import random

gridpoints = [128, 144, 160, 176, 192, 208, 224, 240, 256, 272, 288, 304, 320, 336, 352, 368, 384]
canvas     = 512  # size of the gif in pixels
margin     = 128  # distance from edge of canvas 
num_frames =  16  # number of frames in the animation
step       =   0  # steps in looping animation

# draw the canvas
for frame in range(num_frames):
  newPage(canvas, canvas)
  frameDuration(1/2)
  fill(0.8)
  rect(0, 0, canvas, canvas)
  
  # draw the grid
  fill(None)
  stroke(0.5)
  strokeWidth(1)
  lineCap("round")
  lineJoin("round")
  
  # grid X-axis
  stepx  = -16  # step in sequence on x axis             
  incx   =  16  # grid increment
  for x in range(17):
    save()
    stepx = stepx + incx
    polygon((margin + stepx, margin), (margin+stepx, canvas-margin))
    restore()
    
  # grid Y-axis
  stepy  = -16  # step in sequence on y axis 
  incy   =  16  # grid increment
  for y in range(17):
    save()
    stepy = stepy + incy
    polygon((margin, margin + stepy), (canvas-margin, margin+stepy))
    restore()
    
  # guides
  # stroke(1, 0, 0, 0.4)  
  # strokeWidth(0.5)
  # polygon((0, 128), (512, 128))
  # polygon((0, 128+256), (512, 128+256))
  # polygon((128, 0), (128, 512))
  # polygon((128+256, 0), (128+256, 512))
  # polygon((256, 0), (256, 512))
  # polygon((0, 256), (512, 256))

  # animation loop
  for frame in range(num_frames):
    save()
    a = (random.choice(gridpoints))
    b = (random.choice(gridpoints))
    c = (random.choice(gridpoints))
    fill(1, 1, 1)
    stroke(0.5)
    strokeWidth(1.5)
    oval(c-5, a-5, 10, 10)
    oval(b-5, c-5, 10, 10)
    oval(a-5, b-5, 10, 10)
    restore()
        
saveImage("dbe_2016_02_26_v1.gif")