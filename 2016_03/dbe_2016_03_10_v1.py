#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#  
#                                                                             #
#  Eli Heuer's daily DrawBot exercise!                                        #
#                                                                             #
#  WWW: https://www.tumblr.com/blog/drawbot-exercises                         #
#  Mail: eliheuer@gmail.com                                                   #
#  Drawn on: 03/10/16 -- version 1                                            #
#  Made with DrawBot: http://www.drawbot.com/                                 #
#                                                                             #
#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#

# setting variables
canvas = 512  # size of the gif in pixels
center = int(canvas / 2) - 6 # exact center of the image

bar_range_up = range(0, 264, 8)
bar_range_down = range(248, 0, -8)
bar_range = bar_range_up + bar_range_down 
num_frames = len(bar_range)  # number of frames = length of bar_range list
print bar_range
print len(bar_range)

red_bar_range = [32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256, 248, 240, 232, 224, 216, 208, 200, 192, 184, 176, 168, 160, 152, 144, 136, 128, 120, 112, 104, 96, 88, 80, 72, 64, 56, 48, 40, 32, 24, 16, 8, 0, 8, 16, 24]

orange_bar_range = [64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256, 248, 240, 232, 224, 216, 208, 200, 192, 184, 176, 168, 160, 152, 144, 136, 128, 120, 112, 104, 96, 88, 80, 72, 64, 56, 48, 40, 32, 24, 16, 8, 0, 8, 16, 24, 32, 40, 48, 56]

yellow_bar_range= [96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256, 248, 240, 232, 224, 216, 208, 200, 192, 184, 176, 168, 160, 152, 144, 136, 128, 120, 112, 104, 96, 88, 80, 72, 64, 56, 48, 40, 32, 24, 16, 8, 0, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88]

lightgreen_bar_range = [128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256, 248, 240, 232, 224, 216, 208, 200, 192, 184, 176, 168, 160, 152, 144, 136, 128, 120, 112, 104, 96, 88, 80, 72, 64, 56, 48, 40, 32, 24, 16, 8, 0, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120]

darkgreen_bar_range = [160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256, 248, 240, 232, 224, 216, 208, 200, 192, 184, 176, 168, 160, 152, 144, 136, 128, 120, 112, 104, 96, 88, 80, 72, 64, 56, 48, 40, 32, 24, 16, 8, 0, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152]

lightblue_bar_range = [192, 200, 208, 216, 224, 232, 240, 248, 256, 248, 240, 232, 224, 216, 208, 200, 192, 184, 176, 168, 160, 152, 144, 136, 128, 120, 112, 104, 96, 88, 80, 72, 64, 56, 48, 40, 32, 24, 16, 8, 0, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184]

darkblue_bar_range = [224, 232, 240, 248, 256, 248, 240, 232, 224, 216, 208, 200, 192, 184, 176, 168, 160, 152, 144, 136, 128, 120, 112, 104, 96, 88, 80, 72, 64, 56, 48, 40, 32, 24, 16, 8, 0, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216]

purple_bar_range = [256, 248, 240, 232, 224, 216, 208, 200, 192, 184, 176, 168, 160, 152, 144, 136, 128, 120, 112, 104, 96, 88, 80, 72, 64, 56, 48, 40, 32, 24, 16, 8, 0, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248]

# gird variables
origin = (128, 128)
width = 256
height = 256
num_x_divisions = 8
num_y_divisions = 8
bar_size = width / num_x_divisions

red_bar_x_pos = 0
red_bar_y_pos = 0
red_step = 0
red_bar_x_size = width/num_x_divisions

orange_bar_x_pos = bar_size*1
orange_bar_y_pos = 0
orange_step = 0 
orange_bar_x_size = width/num_x_divisions

yellow_bar_x_pos = bar_size*2
yellow_bar_y_pos = 0
yellow_step = 0 
yellow_bar_x_size = width/num_x_divisions

lightgreen_bar_x_pos = bar_size*3
lightgreen_bar_y_pos = 0
lightgreen_step = 0 
lightgreen_bar_x_size = width/num_x_divisions

darkgreen_bar_x_pos = bar_size*4
darkgreen_bar_y_pos = 0
darkgreen_step = 0 
darkgreen_bar_x_size = width/num_x_divisions

lightblue_bar_x_pos = bar_size*5
lightblue_bar_y_pos = 0
lightblue_step = 0 
lightblue_bar_x_size = width/num_x_divisions

darkblue_bar_x_pos = bar_size*6
darkblue_bar_y_pos = 0
darkblue_step = 0 
darkblue_bar_x_size = width/num_x_divisions

purple_bar_x_pos = bar_size*7
purple_bar_y_pos = 0
purple_step = 0 
purple_bar_x_size = width/num_x_divisions

# draws a new frame in the animation
def new_page(): 
    newPage(canvas, canvas) # new page from canvas variable
    frameDuration(1/24) # set the dividend to desired FPS (frames per second) 
    fill(0.7, 0.7, 0.7)
    rect(0, 0, canvas, canvas) # background

# draws a grid from given arguments    
def grid(origin, width, height, num_x_divisions, num_y_divisions):
    fill(None)
    stroke(0.2) # color
    strokeWidth(1)
    
    translate(*origin)
    step_x = 0 
    increment_x = width / num_x_divisions
    for x in range(num_x_divisions + 1):
        line((step_x, 0), (step_x, height))
        step_x += increment_x
        
    step_y = 0 
    increment_y = height / num_y_divisions
    for y in range(num_y_divisions + 1):
        line((0, step_y), (width, step_y))
        step_y += increment_y
    
# draws the red dot from to position variables    
def red_bar(red_bar_x_pos, red_bar_y_pos, 
    red_bar_x_size, red_bar_y_size):
    fill(0.9, 0.2, 0.1)
    stroke(0.2)
    rect(red_bar_x_pos, red_bar_y_pos, 
        red_bar_x_size, red_bar_y_size)
    
def orange_bar(orange_bar_x_pos, orange_bar_y_pos, 
    orange_bar_x_size, orange_bar_y_size):
    fill(0.9, 0.4, 0.1)
    stroke(0.2)
    rect(orange_bar_x_pos, orange_bar_y_pos, 
        orange_bar_x_size, orange_bar_y_size)
    
def yellow_bar(yellow_bar_x_pos, yellow_bar_y_pos, 
    yellow_bar_x_size, yellow_bar_y_size):
    fill(0.9, 0.9, 0.1)
    stroke(0.2)
    rect(yellow_bar_x_pos, yellow_bar_y_pos, 
        yellow_bar_x_size, yellow_bar_y_size)
    
def lightgreen_bar(lightgreen_bar_x_pos, lightgreen_bar_y_pos, 
    lightgreen_bar_x_size, lightgreen_bar_y_size):
    fill(0.2, 0.8, 0.1)
    stroke(0.2)
    rect(lightgreen_bar_x_pos, lightgreen_bar_y_pos, 
        lightgreen_bar_x_size, lightgreen_bar_y_size)
    
def darkgreen_bar(darkgreen_bar_x_pos, darkgreen_bar_y_pos, 
    darkgreen_bar_x_size, darkgreen_bar_y_size):
    fill(0.1, 0.6, 0.9)
    stroke(0.2)
    rect(darkgreen_bar_x_pos, darkgreen_bar_y_pos, 
        darkgreen_bar_x_size, darkgreen_bar_y_size)

def lightblue_bar(lightblue_bar_x_pos, lightblue_bar_y_pos, 
    lightblue_bar_x_size, lightblue_bar_y_size):
    fill(0.1, 0.3, 0.9)
    stroke(0.2)
    rect(lightblue_bar_x_pos, lightblue_bar_y_pos, 
        lightblue_bar_x_size, lightblue_bar_y_size)
    
def darkblue_bar(darkblue_bar_x_pos, darkblue_bar_y_pos, 
    darkblue_bar_x_size, darkblue_bar_y_size):
    fill(0.5, 0.1, 0.9)
    stroke(0.2)
    rect(darkblue_bar_x_pos, darkblue_bar_y_pos, 
        darkblue_bar_x_size, darkblue_bar_y_size)
    
def purple_bar(purple_bar_x_pos, purple_bar_y_pos, 
    purple_bar_x_size, purple_bar_y_size):
    fill(0.85, 0.1, 0.7)
    stroke(0.2)
    rect(purple_bar_x_pos, purple_bar_y_pos, 
        purple_bar_x_size, purple_bar_y_size)
    
# draw each frame as a new page
for frame in range(num_frames):
    new_page() 
    
    # draw the grid
    grid(origin, width, height, num_x_divisions, num_y_divisions)
    
    # type -- future idea: print out variable data?
    fontSize(32)
    font("Helvetica Neue Bold")
    tracking(-1.2)
    fill(0.2)
    stroke(None)
    text("Hello World", (-2, -32))
    
    red_bar_y_size = red_bar_range[red_step]
    orange_bar_y_size = orange_bar_range[orange_step]
    yellow_bar_y_size = yellow_bar_range[yellow_step]
    lightgreen_bar_y_size = lightgreen_bar_range[lightgreen_step]
    darkgreen_bar_y_size = darkgreen_bar_range[darkgreen_step]
    lightblue_bar_y_size = lightblue_bar_range[lightblue_step]
    darkblue_bar_y_size = darkblue_bar_range[darkblue_step]
    purple_bar_y_size = purple_bar_range[purple_step]

    red_bar(red_bar_x_pos, red_bar_y_pos, 
        red_bar_x_size, red_bar_y_size)   
    red_step += 1

    orange_bar(orange_bar_x_pos, orange_bar_y_pos, 
        orange_bar_x_size, orange_bar_y_size)   
    orange_step += 1
    
    yellow_bar(yellow_bar_x_pos, yellow_bar_y_pos, 
        yellow_bar_x_size, yellow_bar_y_size)   
    yellow_step += 1
    
    lightgreen_bar(lightgreen_bar_x_pos, lightgreen_bar_y_pos, 
        lightgreen_bar_x_size, lightgreen_bar_y_size)   
    lightgreen_step += 1
    
    darkgreen_bar(darkgreen_bar_x_pos, darkgreen_bar_y_pos, 
        darkgreen_bar_x_size, darkgreen_bar_y_size)   
    darkgreen_step += 1
    
    lightblue_bar(lightblue_bar_x_pos, lightblue_bar_y_pos, 
        lightblue_bar_x_size, lightblue_bar_y_size)   
    lightblue_step += 1
    
    darkblue_bar(darkblue_bar_x_pos, darkblue_bar_y_pos, 
        darkblue_bar_x_size, darkblue_bar_y_size)   
    darkblue_step += 1
    
    purple_bar(purple_bar_x_pos, purple_bar_y_pos, 
        purple_bar_x_size, purple_bar_y_size)   
    purple_step += 1
    
saveImage("dbe_2016_03_10_v1.gif")