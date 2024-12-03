f = open("day_3/input.txt")
data = f.read()

def coolInput(line) :
    temp = ""
    done = False
    val1, val2 = 0, 0
    for x in line :
        if done == False : 
            if x == ',' :
                val1 = temp
                temp = ""
            elif x == ')' :
                val2 = temp
                done = True
            elif x.isnumeric() :
                temp += x

    if temp == "" or int(val1) > 999 or int(val2) > 999 :
        val1, val2 = 0, 0
    return val1, val2


# check if there is mul(x,y)
# also check for do and don't commands
total = 0
foundId = [-1]
do = True

for x in range(len(data)) :
    foundAt = data.find("mul(",x)
    # from foundAt to x last do/dont command
    foundDoAt = data.rfind("do()", x, foundAt)
    foundDontAt = data.rfind("don't()", x, foundAt)

    if foundDoAt < foundDontAt :
        do = False
    elif foundDoAt > foundDontAt :
        do = True

    if foundAt not in foundId and do:
        # mul( found, now check for numbers
        num1, num2 = coolInput(data[foundAt+3:foundAt+13])
        total += int(num1)*int(num2)
        x = foundAt    
        foundId.append(foundAt)
print(total)