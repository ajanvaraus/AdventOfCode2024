def check(levels) :
    safeAsc = 0
    safeDes = 0
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
        return 1
    else : 
        return 0
    
f = open("day_2/report.txt")
reports = []
safeTotal = 0

# creating a list
# comparing the numbers on the list
for line in f :
    levels = line.split()

    if check(levels) == 1 :
        safeTotal += 1
    else :
        found = False
        for x in range(len(levels)) :
            y = levels.copy()
            del y[x]
            if check(y) == 1 and found == False:
                safeTotal += 1
                found = True

print(safeTotal)

