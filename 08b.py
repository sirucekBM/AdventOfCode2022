

#Strom je viditelný, pokud jsou všechny ostatní stromy mezi ním a okrajem mřížky kratší než on

with open("08data.txt") as data:
    listX = data.readlines()


pocetR = len(listX)
pocetC = len(listX[0])-1

print("počet řádků: " + str(pocetR))
print("počet sloupců: " + str(pocetC))

pocetObvod = ((pocetC*2) +(pocetR*2))-4
print("počet obvod: " + str(pocetObvod))


def kontrolaViditelnosti(cislo, startR,startC, arr):

    pocetR = len(arr)
    pocetC = len(arr[0])
    vysledek = 0
    nahoru = 0
    dolu = 0
    doleva = 0
    doprava = 0



    #-----jdu do prava-----------
    x = range(startC+1, pocetC)
    for n in x:
        tempC = arr[startR][n]
        if(tempC>=cislo):
            doprava += 1
            break
        else:
            doprava += 1


    #-----jdu do leva---------------
    x = range(startC - 1, -1,-1)
    for n in x:
        tempC = arr[startR][n]
        if(tempC>=cislo):
            doleva += 1
            break
        else:
            doleva += 1


    #-----jdu nahoru-----------
    x = range(startR- 1, -1,-1)
    for n in x:
        tempC = arr[n][startC]
        if(tempC>=cislo):
            nahoru += 1
            break
        else:
            nahoru += 1

    #-----jdu dolu---------
    x = range(startR + 1, pocetR)
    for n in x:
        tempC = arr[n][startC]
        if(tempC>=cislo):
            dolu += 1
            break
        else:
            dolu += 1

    vysledek = nahoru * dolu * doleva * doprava

    return vysledek

#----------data nahraji do matice---------------
arr=[]
rows, cols = (len(listX), len(listX[0]))
for i in listX:
    col = []
    for j in i:
        if('\n' not in j):
            col.append(int(j))
    arr.append(col)
#---------------------------------------------

#------------budu procházet matici--------
pocetViditelnych = 0
rowIndex = 0
m = range(1, pocetR-1)
maxScore = 0
for r in m:
    cIndex = 1
    x = range(cIndex, pocetC-1)
    for n in x:
        cislo = arr[r][cIndex]
        scenickeScore = kontrolaViditelnosti(cislo,r,cIndex, arr)
        if(scenickeScore > maxScore):
            maxScore = scenickeScore
            poziceRad = r+1
            poziceCol = n
            stromCislo = cislo
        
        cIndex += 1


print("max skore: " + str(maxScore))
print("na řádku: " + str(poziceRad))
print("ve sloupci: " + str(poziceCol))
print("číslo stromu: " + str(stromCislo))

#první pokus = 327180 byl dobře
#řádek 57 sloupec 84
#čas programování 10 minut