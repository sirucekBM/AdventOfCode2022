

with open("03data.txt") as data:
    lines = data.readlines()


#Typy položek s malými písmeny a až z  mají priority 1 až 26.
#Typy položek s velkými písmeny A až Z mají priority 27 až 52.

mala="abcdefghijklmnopqrstuvwxyz"
velka="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

seznamShod=[]
for textX in lines:
    celkem = len(textX )
    polovina = int(celkem/2) 
    veciA=textX[:polovina]
    veciB=textX[polovina:] 

    for x in veciA:
        if(x[0] in veciB):
            seznamShod.append(x)
            break

celkem=0
for pismeno in seznamShod:
    px=pismeno[0]
    indexM = mala.find(px)+1
    indexV = velka.find(px)+27
    if(indexV==26):
        indexV=0

    celkem += indexM + indexV

print(celkem)
# první pokus = 16932 byl špatně, druhý pokus = 11770 byl taky špatně, třetí pokus = 3970 byl taky špatně
# čtvrtý pokus = 7766 a ten byl dobře





