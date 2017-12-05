# It has something to do with the diagonal line, it is all powers of uneven numbers
import math


inputNumber = 325489

square = math.ceil(math.sqrt(inputNumber))
corner = int(math.pow(square, 2))

smallside = square-1
if(corner-smallside) <= inputNumber <= corner:
    center = corner - int(math.floor(square/2))
elif(corner-2*smallside) <= inputNumber <= corner:
    center = corner - smallside - int(math.floor(square/2))
elif(corner-3*smallside) <= inputNumber <= corner:
    center = corner - smallside - int(math.floor(square / 2))
else:
    center = corner - smallside - int(math.floor(square / 2))


sidedistance = abs(center-inputNumber)
total = int(math.floor(square/2)) + sidedistance
print(total)



# Part 2:
# after hours of trying to find a mathematical solution, here the brute force way:
#
#

value = 1
x = 0
y = 0
grid = {(x, y): value}


direction = 0
side_step = 0
side_length = 1
side_once = False

while value < inputNumber:
    if direction == 0:
        x += 1
    elif direction == 1:
        y += 1
    elif direction == 2:
        x -= 1
    else:
        y -= 1

    new_value = sum([grid[x+a, y+b] for a in [-1, 0, 1] for b in [-1, 0, 1] if (x+a, y+b) in grid])
    grid[(x, y)] = new_value
    value = new_value
    side_step += 1

    if side_step == side_length:
        direction = (direction + 1) % 4
        side_step = 0
        if side_once:
            side_length += 1
            side_once = False
        else:
            side_once = True

print(value)
