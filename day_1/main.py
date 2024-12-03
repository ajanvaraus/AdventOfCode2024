# part 1
f = open("input.txt")
listA = []
listB = []
distance = 0

# readline
# split
# append
for line in f :
    numbers = line.split()
    listA.append(int(numbers[0]))
    listB.append(int(numbers[1]))

# sort arrays
listA.sort()
listB.sort()

# add to distance
for x in range(len(listA)) :
    distance += abs(listA[x] - listB[x])

# print distance
print(distance)

# part 2
similarity = 0
# read lines into lists
# for loop (go through A and compare it to every number in B)

for numA in listA :
    count = 0
    for numB in listB :
        if numA == numB :
            count += 1
    similarity += count * numA
    count = 0
print(similarity)