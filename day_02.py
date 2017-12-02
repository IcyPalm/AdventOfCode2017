import sys

import itertools

checksumList = []
with open("inputs/day_02.txt") as f:
    for line in f:
        maxNum = -sys.maxsize
        minNum = sys.maxsize
        values = line.split("\t")
        for value in values:
            intValue = int(value)
            maxNum = max(maxNum, intValue)
            minNum = min(minNum, intValue)
        checksumList.append(abs(maxNum-minNum))

print(sum(checksumList))

divisionList = []
with open("inputs/day_02.txt") as f:
    for line in f:
        values = [int(n) for n in line.split()]

        for i in range(len(values)):
            for j in range(len(values)):
                if i==j:
                    continue
                if values[i] % values[j] == 0:
                    divisionList.append(values[i] / values[j])

print(int(sum(divisionList)))

