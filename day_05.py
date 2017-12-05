with open("inputs/day_05.txt") as f:
    lines = f.readlines()

numbers = []
for line in lines:
    numbers.append(int(line))

steps = 0
position = 0

while 0 <= position <= len(numbers) - 1:
    next_position = position + numbers[position]
    numbers[position] += 1
    steps += 1
    position = next_position

print(steps)

# Part 2:
numbers = []
for line in lines:
    numbers.append(int(line))
steps = 0
position = 0

while 0 <= position <= len(numbers) - 1:
    next_position = position + numbers[position]
    if numbers[position] >= 3:
        numbers[position] -= 1
    else:
        numbers[position] += 1
    steps += 1
    position = next_position

print(steps)
