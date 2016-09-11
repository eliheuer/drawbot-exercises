# first try at a drawbot twitch stream

import math

# static variables
canvas = 256
num_frames = 63
center = 128

# path variables
path_x = 0
path_y = 0

# box variables
box_size_x = 24
box_size_y = 24
box_amp = 24
box_step = 0
box_count = 70

def new_page():
    newPage(canvas, canvas)
    frameDuration(1/24)
def box(x_pos, y_pos, box_size_x, box_size_y):
    fill(0.95)
    strokeWidth(0.5)
    stroke(0.3)
    rotate(6)
    rect((x_pos - 2) + center/4, (y_pos - 2) + center/4,
        box_size_x, box_size_y)

def draw_path(path_x, path_y, box_count, box_amp, box_step):
    for segment in range(box_count):
        box_x = math.cos(box_step) * box_amp/2
        box_y = math.sin(box_step) * box_amp/2
        box(box_x, box_y, box_size_x, box_size_y)
        box_step += 0.05 * math.pi

for frame in range(num_frames):
    new_page()
    translate(128, 128)
    draw_path(path_x, path_y, box_count, box_amp, box_step)
    box_step += 0.1

saveImage("twitch.gif")