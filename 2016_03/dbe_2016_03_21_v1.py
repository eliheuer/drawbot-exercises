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
num_frames = 64

# gird variables
origin = (128, 128)
width = 256
height = 256
center = width/2
num_x_units = 8
num_y_units = 8

# box variables
dot_size_x = 32
dot_size_y = 32
dot_x = 0
dot_y = 0

#itertools
seq_up = [5, 30, 40, 50, 60, 70, 80, 90, 100, 105, 110, 114, 116, 118, 119, 120]
seq_dn = [119, 118, 116, 114, 110, 105, 100, 90, 80, 70, 60, 50, 40, 30, 20, 0]

seq_x_up_size = [32, 32, 36, 34, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32]
seq_x_dn_size = [32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 30, 30, 60, 60, 40]

seq_y_up_size = [32, 40, 38, 36, 34, 32, 32, 32, 32, 32, 32, 32, 32, 30, 30, 30]
seq_y_dn_size = [32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 34, 36, 40, 40, 28, 28]

seq = seq_up + seq_dn
seq_x_size = seq_x_up_size + seq_x_dn_size
seq_y_size = seq_y_up_size + seq_x_dn_size

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
    
    oval((dot_x - dot_size_x/2) + center, (dot_y-128) + center, dot_size_x, dot_size_y) 
    
    dot_y_string = "{:.1f}".format(dot_y)
        
    # type 
    fontSize(32)
    font("Helvetica Neue Bold")
    fill(1, 1, 1)
    stroke(None)
    text("Y Position:", (-2, -32))
    text("Frame Count:", (-2, -64))
    fill(1, 0, 0)
    text(dot_y_string, (170, -32))
    text(dot_y_string, (220, -64))
    
saveImage("dbe_2016_03_21_v1.gif")