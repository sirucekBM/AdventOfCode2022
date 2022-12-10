lines=[]
with open("05data.txt") as data:
    for line in data:
        if('move' in line):
            lines.append(line)

"""
    [P]                 [Q]     [T]
[F] [N]             [P] [L]     [M]
[H] [T] [H]         [M] [H]     [Z]
[M] [C] [P]     [Q] [R] [C]     [J]
[T] [J] [M] [F] [L] [G] [R]     [Q]
[V] [G] [D] [V] [G] [D] [N] [W] [L]
[L] [Q] [S] [B] [H] [B] [M] [L] [D]
[D] [H] [R] [L] [N] [W] [G] [C] [R]
 1   2   3   4   5   6   7   8   9 
"""
stack1 =['D','L','V','T','M','H','F']
stack2 =['H','Q','G','J','C','T','N','P']
stack3 =['R','S','D','M','P','H']
stack4 =['L','B','V','F']
stack5 =['N','H','G','L','Q']
stack6 =['W','B','D','G','R','M','P']
stack7 =['G','M','N','R','C','H','L','Q']
stack8 =['C','L','W']
stack9 =['R','D','L','Q','J','Z','M','T']

listStacks=[]
listStacks.append(stack1)
listStacks.append(stack2)
listStacks.append(stack3)
listStacks.append(stack4)
listStacks.append(stack5)
listStacks.append(stack6)
listStacks.append(stack7)
listStacks.append(stack8)
listStacks.append(stack9)

#move 1 from 7 to 6

for vstup in lines:
    tokens = vstup.split(' ')
    pocet = int(tokens[1].strip())
    zHromady = int(tokens[3].strip())
    naHromadu = int(tokens[5].strip())
    tempList = []

    for c in range(pocet):
        tempList.append(listStacks[zHromady-1].pop())

    tempList.reverse()
    for c in tempList:
        print('----zacinam-------')
        print(listStacks[zHromady-1])
        print(listStacks[naHromadu-1])
        bedna = c
        print(bedna)
        listStacks[naHromadu-1].append(bedna)
        print(listStacks[zHromady-1])
        print(listStacks[naHromadu-1])

for st in listStacks:
    print(st[-1],end='')

# první pokus = HNSNMTLHQ byl správně
#doba řešení = 30 minnut
