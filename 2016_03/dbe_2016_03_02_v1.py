import math

print "start"

def dot_sin(beat):
    dot_sin = (math.sin(beat/8))
    #dot_sin = int(round(dot_sin*4))
    print dot_sin

beat = 0

for i in range(32):
    beat = beat + 1
    dot_sin(beat)

print "end"