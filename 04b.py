
with open("04data.txt") as data:
    lines = data.readlines()

counter = 0
r=0
for xt in lines:
    tokens =xt.split(',')
    tokensA = tokens[0].split('-')
    tokensB = tokens[1].split('-')
    elfA1 = int(tokensA[0].strip())
    elfA2 = int(tokensA[1].strip())
    elfB1 = int(tokensB[0].strip())
    elfB2 = int(tokensB[1].strip())

    r +=1
    
    if(elfB1 >= elfA1 and elfB1 <= elfA2):
        counter +=1
        continue
    if(elfB2 >= elfA1 and elfB2 <= elfA2):
        counter +=1
        continue

    if(elfA1 >= elfB1 and elfA1 <= elfB2):
        counter +=1
        continue
    if(elfA1 >= elfB1 and elfA2 <= elfB2):
        counter +=1


#první pokus = 806  byl dobře
#doba řešení = 5 minnut
print(counter)