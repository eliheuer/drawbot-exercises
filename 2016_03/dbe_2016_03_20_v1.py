#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#  
#                                                                             #
#  Eli Heuer's daily DrawBot exercise!                                        #
#                                                                             #
#  Web: https://www.tumblr.com/blog/drawbot-exercises                         #
#  Mail: eliheuer@gmail.com                                                   #
#  Drawn on: 03/20/16 -- version 1                                            #
#  Made with DrawBot: http://www.drawbot.com/                                 #
#                                                                             #
#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#

# from drawBot import * # uncomment if using setupAsModule.py
import math 
import itertools 

# static variables
canvas = 512 
num_frames = 126

# gird variables
origin = (128, 128)
width = 256
height = 256
center = width/2
num_x_units = 8
num_y_units = 8

# path variables
path_x = 0
path_y = 0
divisions = 0

# box variables
dot_size_x = 20
dot_size_y = 20
dot_amp = 120
dot_step = 0
dot_count = 1
dot_shift = 0

#itertools
seq_up = range(4, 256, 4)
seq_dn = range(256, 4, -4)
seq = seq_up + seq_dn
print seq
seq_step = itertools.cycle(seq)

def new_page(): 
    newPage(canvas, canvas) 
    frameDuration(1/24) 
    fill(0.025, 0.025, 0.1) 
    rect(0, 0, canvas, canvas) 
        
def dot(dot_x, dot_y, dot_size_x, dot_size_y, fill):
    stroke(None)
    oval((dot_x - 2) + center, (dot_y - 2) + center, dot_size_x, dot_size_y)
    
def draw_path(path_x, path_y, dot_count, dot_amp, dot_step, fill):
    for segment in range(dot_count):
        dot_x = math.cos(dot_step) * dot_amp
        dot_y = math.sin(dot_step) * dot_amp
        dot(dot_x-8, dot_y-8, dot_size_x, dot_size_y, fill)     
        dot_step += 0.01 * math.pi
       
def grid(origin, width, height, num_x_units, num_y_units):
    translate(*origin)
    strokeWidth(1)
    stroke(0.025, 0.025, 0.1)  
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
    draw_path(path_x, path_y, dot_count, dot_amp, dot_step+dot_shift*6, fill)
    fill(0.9, 0.25, 0.1)
    draw_path(path_x, path_y, dot_count, dot_amp-24, dot_step+dot_shift*5, fill)
    fill(0.9, 0.4, 0.1)
    draw_path(path_x, path_y, dot_count, dot_amp-48, dot_step+dot_shift*4, fill)
    fill(0.9, 0.6, 0.1)
    draw_path(path_x, path_y, dot_count, dot_amp-72, dot_step+dot_shift*3, fill)
    fill(0.9, 0.8, 0.1)
    draw_path(path_x, path_y, dot_count, dot_amp-96, dot_step+dot_shift*2, fill)
    fill(0.9, 0.9, 0.3)
    stroke(None)
    oval(center-10, center-10, dot_size_x, dot_size_y)
    dot_step += 0.1
    dot_shift += 0.1
    dot_count = seq_step.next()
    dot_count_string = "{:.1f}".format(dot_count)
        
    # type 
    # fontSize(24)
    # font("Helvetica Neue Bold")
    # fill(1, 1, 1)
    # stroke(None)
    # text("Dot Count:", (-2, -32))
    # fill(1, 0, 0)
    # text(dot_count_string, (-2, -64))
    
saveImage("dbe_2016_03_20_v1.gif")