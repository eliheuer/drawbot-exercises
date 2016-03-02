import math

print "start"

def dot(step):
    x = (math.cos(step*8))
    x = int(round(x*4))
    print x 
    
step = 0

for i in range(32):
    step = step + 1
    dot(step)

print "end"