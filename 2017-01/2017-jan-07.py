# GIF file rendered with DrawBot: http://www.drawbot.com/

import math 
import itertools 

# static variables
canvas = 512 
num_frames = 60

# gird variables
origin = (128, 128)
width = 256
height = 256
center = width/2
num_x_units = 16
num_y_units = 16

# dot variables
dot_size_x = 20
dot_size_y = 20
dot_amp = 120
dot_step = 0
dot_count = 1
dot_shift = 0

#itertools
seq_up = range(2, 60, 2)
seq_dn = range(60, 2, -2)
seq = seq_up + seq_dn
print seq
seq_step = itertools.cycle(seq)

def new_page(): 
    newPage(canvas, canvas) 
    frameDuration(1/24) 
    fill(0.1) 
    rect(0, 0, canvas, canvas) 
        
def dot(dot_x, dot_y, dot_size_x, dot_size_y, fill):
    stroke(None)
    oval((dot_x - 2) + center, (dot_y - 2) + center, dot_size_x, dot_size_y)
    
def draw_path(dot_count, dot_amp, dot_step):
    for segment in range(dot_count):
        dot_x = math.cos(dot_step) * dot_amp
        dot_y = math.sin(dot_step) * dot_amp
        dot(dot_x-8, dot_y-8, dot_size_x, dot_size_y, fill)     
        dot_step += 0.012 * math.pi
        
def draw_path_rev(dot_count, dot_amp, dot_step):
    for segment in range(dot_count):
        dot_x = math.cos(dot_step) * dot_amp
        dot_y = math.sin(dot_step) * dot_amp
        dot(dot_x-8, dot_y-8, dot_size_x, dot_size_y, fill)     
        dot_step -= 0.012 * math.pi
       
def grid(origin, width, height, num_x_units, num_y_units):
    translate(*origin)
    strokeWidth(1)
    stroke(0.2)  
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
    
    fill(0.9, 0.2, 0.1)
    draw_path(dot_count, dot_amp, dot_step+dot_shift)
    
    fill(0.9, 0.4, 0.1)
    draw_path(dot_count, dot_amp-24, dot_step+dot_shift+0.2)
    
    fill(0.9, 0.9, 0.1)
    draw_path(dot_count, dot_amp-48, dot_step+dot_shift+0.4)
    
    fill(0.2, 0.8, 0.1)
    draw_path(dot_count, dot_amp-72, dot_step+dot_shift+0.6)
    
    fill(0.1, 0.6, 0.9)
    draw_path(dot_count, dot_amp-96, dot_step+dot_shift+0.8)
    
    # fill(0.1, 0.3, 0.9)
    # oval(center-10, center-10, dot_size_x, dot_size_y)
    
    dot_step += 0.395
    dot_shift += 0.01
    dot_count = seq_step.next()
        
saveImage("2017-jan-06.gif")