#  Eli Heuer's daily DrawBot exercise!
#  eliheuer@gmail.com
#  02/27/16 -- version 2
#  Made with DrawBot:
#  http://www.drawbot.com/ 

# pep-8 maximum-line-length #/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#

# setting up the canvas size and main variables

canvas      = 512  # size of the gif in pixels
margin      = 128  # distance from edge of canvas 
num_frames  =  16  # number of frames in the animation
stepa       =  -1  # steps in looping animation
stepb       =  17  # steps in looping animation
stepc       =  -9  # steps in looping animation
stepd       =   8  # steps in looping animation
circle_size =  14  # self explanatory

# grid increments (16px X 16pc)
gridpoints = range(128, 400, 16) 
gridpoints_reverse = gridpoints[::-1]
print gridpoints
print gridpoints_reverse


# draw the canvas
for frame in range(num_frames):
  newPage(canvas, canvas)
  stepa = stepa + 1
  stepb = stepb - 1
  stepc = stepc + 1
  stepd = stepd - 1
  frameDuration(1/20)
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
  # stroke(0.4)  
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
    a = gridpoints[stepa]
    b = gridpoints[stepb]
    c = gridpoints_reverse[stepc]
    d = gridpoints_reverse[stepd]
    fill(1)
    strokeWidth(1.5)
    stroke(0.5)
    
    # outer going in 
    oval(a-(circle_size/2), a-(circle_size/2), circle_size, circle_size)
    oval(b-(circle_size/2), b-(circle_size/2), circle_size, circle_size)
    oval(a-(circle_size/2), b-(circle_size/2), circle_size, circle_size)
    oval(b-(circle_size/2), a-(circle_size/2), circle_size, circle_size)
    
    #inner going out
    oval(c-(circle_size/2), c-(circle_size/2), circle_size, circle_size)
    oval(d-(circle_size/2), 256-(circle_size/2), circle_size, circle_size)
    oval(c-(circle_size/2), d-(circle_size/2), circle_size, circle_size)
    oval(d-(circle_size/2), 256-(circle_size/2), circle_size, circle_size)
    
    restore()
      
saveImage("dbe_2016_02_27_v2.gif")