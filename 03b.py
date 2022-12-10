with open("03data.txt") as data:
    lines = data.readlines()

abeceda="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

counter = 0
celkem=0
listX=[]

for xt in lines:
    listX.append(xt)
    counter +=1
    if(counter==3):
        counter =0
        elf1=listX[0].strip()
        elf2=listX[1].strip()
        elf3=listX[2].strip()

        for x in elf1:
            if(x[0] in elf2 and x[0] in elf3):
                indexABCD =abeceda.find(x[0])+1
                celkem += indexABCD
                break

        listX=[]

print(celkem)
# první pokus = 2415 byl správně
