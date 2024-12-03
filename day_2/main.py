f = open("day_2/report.txt")
reports = []
safeTotal = 0

# creating a list
# comparing the numbers on the list
for line in f :
    safeAsc = 0
    safeDes = 0
    levels = line.split()

    tempLevel = levels[0]

    for level in levels :
        levels[levels.index(level)] = int(level)
        level = int(level)

        if (levels.index(level) != 0) :
            if tempLevel < level and level-tempLevel <= 3:
                safeAsc += 1
                safeDes = 0
            elif tempLevel > level and tempLevel-level <= 3:
                safeDes += 1
                safeAsc = 0
        
        tempLevel = level

    if safeAsc == len(levels)-1 or safeDes == len(levels)-1 :
        safeTotal += 1

print(safeTotal)
