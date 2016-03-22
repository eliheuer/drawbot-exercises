my_list = []
x = 0
y = 16 
a = 0 

for i in range(16):
    a = x + y
    my_list.append(a)
    x = a
    y -= 1 

print my_list