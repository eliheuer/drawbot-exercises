#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#  
#                                                                             #
#  Eli Heuer's daily DrawBot exercise!                                        #
#                                                                             #
#  Web: https://www.tumblr.com/blog/drawbot-exercises                         #
#  Mail: eliheuer@gmail.com                                                   #
#  Drawn on: 03/21/16 -- version 1                                            #
#  Made with DrawBot: http://www.drawbot.com/                                 #
#                                                                             #
#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#

# from drawBot import * # uncomment if using setupAsModule.py
import itertools 

# static variables
canvas = 512 
num_frames = 32

# gird variables
origin = (128, 128)
width = 256
height = 256
center = width/2
num_x_units = 8
num_y_units = 8

# dox variables
dot_size_x = 32
dot_size_y = 32
dot_x = 0
dot_y = 0
dot_amp = 1.5 # adjusts how high the ball bounces, try 0.5, 1, 4, etc...

#itertools
seq_up = [5, 25, 50, 70, 90, 100, 110, 116, 122, 126, 130, 132, 134, 135, 136, 136]
seq_dn = [136, 135, 134, 132, 130, 126, 122, 116, 110, 100, 90, 70, 50, 20, 0, 0]

seq_x_up_size = [28, 30, 31, 31, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32]
seq_x_dn_size = [32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 30, 42]

seq_y_up_size = [44, 44, 42, 40, 38, 36, 34, 33, 32, 32, 32, 32, 32, 32, 32, 32]
seq_y_dn_size = [32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 34, 38, 28]

seq = seq_up + seq_dn
seq_x_size = seq_x_up_size + seq_x_dn_size
seq_y_size = seq_y_up_size + seq_y_dn_size

print seq
print seq_x_size
print seq_y_size
print len(seq_x_size)
print len(seq_y_size)
print len(seq)

seq_step = itertools.cycle(seq)
seq_x_size_step = itertools.cycle(seq_x_size)
seq_y_size_step = itertools.cycle(seq_y_size)

def new_page(): 
    newPage(canvas, canvas) 
    frameDuration(1/24) 
    fill(0.025, 0.025, 0.1) 
    rect(0, 0, canvas, canvas) 
    
def grid(origin, width, height, num_x_units, num_y_units):
    translate(*origin)
    strokeWidth(1)
    stroke(1, 1, 1)  
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
        
for frame in range(num_frames):
    new_page()
    grid(origin, width, height, num_x_units, num_y_units)
    fill(0.9, 0, 0.1)
    stroke(None)
    
    dot_size_x = seq_x_size_step.next()
    dot_size_y = seq_y_size_step.next()
    dot_y = seq_step.next()
    oval((dot_x - dot_size_x/2) + center, ((dot_y * dot_amp) - 128) + center, 
        dot_size_x, dot_size_y) 
    
    # type 
    dot_size_y_string = "{:03d}".format(dot_size_y)
    dot_size_x_string = "{:03d}".format(dot_size_x)
    dot_y_string = "{:03d}".format(dot_y)
    fontSize(24)
    font("input mono")
    fill(1, 1, 1)
    stroke(None)
    text("y_position:", (-1, -32))
    text("squash:", (-1, -64))
    text("stretch:", (-1, -96))
    fill(0.9, 0, 0.1)
    text(dot_y_string, (214, -32))
    text(dot_size_x_string, (214, -64))
    text(dot_size_y_string, (214, -96))
    
saveImage("dbe_2016_03_21_v1.gif")