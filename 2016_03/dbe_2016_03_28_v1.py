#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/# 
#                                                     #
#  Eli Heuer's daily DrawBot exercise!                #
#                                                     #
#  Web: http://drawbot-exercises.tumblr.com/          #
#  Mail: eliheuer@gmail.com                           #
#  Drawn on: 03/28/16 -- version 1                    #
#  Made with DrawBot: http://www.drawbot.com/         #
#                                                     #
#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#

from drawBot import * # if using setupAsModule.py
import math 
import itertools
import random

# static variables
canvas = 512 
num_frames = 60
angle_delta = 2*math.pi/num_frames

# gird variables
origin = (128, 128)
width = 256
height = 256
center = width/2
num_x_units = 8
num_y_units = 8

# dot variables
dot_size_x = 20
dot_size_y = 20
dot_angle = 0
dot_count = 1
dot_shift = 0
num_dots = 4

def new_page():
    newPage(canvas, canvas) 
    frameDuration(1/24) 
    fill(0.1, 0.1, 0.2) 
    rect(0, 0, canvas, canvas)

def dot(dot_x, dot_y, dot_size_x, dot_size_y):
    stroke(None)
    oval((dot_x-2)+center, (dot_y-2)+center,
         dot_size_x, dot_size_y)
    
def draw_path(arc_start, arc_end, dot_radius):
    current_angle = arc_start_angle
    while current_angle <= arc_end_angle:
        dot()
        current_angle += delta
    
    for segment in range(dot_count):
        dot_x = math.cos(dot_angle) * dot_amp
        dot_y = math.sin(dot_angle) * dot_amp
        dot(dot_x-8, dot_y-8, dot_size_x, dot_size_y)     
        dot_angle += 0.0083 * math.pi
        
def grid(origin, width, height, num_x_units, num_y_units):
    translate(*origin)
    strokeWidth(1)
    stroke(0.5, 0.5, 0.7)  
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

    for d in range(num_dots):

        r = random.random()
        g = random.random()
        b = random.random()
        fill(r, g, b)
        
        dot_radius = d*24
        draw_path(dot_start, dot_end, dot_radius)
        dot_start = 45 + d
        dot_end = 90 + d
       
    dot_angle += angle_delta
    
saveImage("dbe_2016_03_28_v1.pdf")
