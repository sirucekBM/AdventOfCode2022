

with open("01data.txt") as data:
    lines = data.readlines()

tempSum = 0
elf = 1
seznam ={}
maxCal = 0
highElf = 1
listCalories = []
for d in lines:
    if(len(d)>1):
        tempSum += int(d)
    else:
        seznam[elf] = tempSum
        listCalories.append(tempSum)
        list
        if(tempSum>maxCal):
            maxCal = tempSum
            highElf = elf

        elf +=1
        tempSum = 0

seznamSorted = dict(sorted(seznam.items(), key=lambda item: item[1],reverse=True))
listCalories.sort(reverse=True)


triElf = listCalories[0] + listCalories[1] + listCalories[2]



print("nejvíc nese: " + str(highElf) + " celkem: " + str(maxCal))
print("součet tří nejvíce: " + str(triElf))