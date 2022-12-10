

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
    vysledek = False
    nahoru = 1
    dolu = 1
    doleva = 1
    doprava = 1



    #-----jdu do prava-----------
    x = range(startC+1, pocetC)
    for n in x:
        tempC = arr[startR][n]
        if(tempC>=cislo):
            doprava = 0
            break


    #-----jdu do leva---------------
    x = range(startC - 1, -1,-1)
    for n in x:
        tempC = arr[startR][n]
        if(tempC>=cislo):
            doleva = 0
            break


    #-----jdu nahoru-----------
    x = range(startR- 1, -1,-1)
    for n in x:
        tempC = arr[n][startC]
        if(tempC>=cislo):
            nahoru = 0
            break


    #-----jdu dolu---------
    x = range(startR + 1, pocetR)
    for n in x:
        tempC = arr[n][startC]
        if(tempC>=cislo):
            dolu = 0
            break

    soucet = nahoru + dolu + doleva + doprava
    if(soucet >0 ):
        vysledek = True

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
for r in m:
    cIndex = 1
    x = range(cIndex, pocetC-1)
    for n in x:
        cislo = arr[r][cIndex]
        #print(cislo)
        jeVidet = kontrolaViditelnosti(cislo,r,cIndex, arr)
        #print(jeVidet)
        if(jeVidet):
            pocetViditelnych += 1
        cIndex += 1


print("počet viditelných: " + str(pocetViditelnych + pocetObvod))

#první pokus = 1672 byl dobře
#čas programování 30minut