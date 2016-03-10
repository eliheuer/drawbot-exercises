
import math # for cos and sin functions

# static variables
canvas = 512  # size of the gif in pixels
num_frames = 16  # number of frames in the animation

# draws a new frame in the animation
def new_page(): 
    newPage(canvas, canvas) # new page from canvas variable
    frameDuration(1/24) # set the dividend to desired FPS (frames per second) 
    fill(0.7, 0.7, 0.7) #dark grey
    rect(0, 0, canvas, canvas) # background

def fib(n):
    stroke(1)
    line((0, 0), (30, 0))
    turtle.forward(30)
    
    if n<2:
        pass
    else:
        line((0, 0), (30, 0))
        fib(n-1)
        line((0, 0), (30, 30))
        fib(n-2)
        line((0, 0), (30, 30))

    translate(30, 30)

# draw each frame as a new page
for frame in range(num_frames):
    new_page() 
    fib(10)

saveImage("dbe_2016_03_10_v2.gif")