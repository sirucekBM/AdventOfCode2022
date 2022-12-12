with open("data\\09data.txt") as data:
    listX = data.readlines()



aktualPoziceOcas = {'X':0,'Y':0}
aktualPoziceHlava = {'X':0,'Y':0}
tempPozice = {'X':0,'Y':0}
listPozic=[]


pocetL = 0
pocetR = 0
pocetU = 0
pocetD = 0

def porovnejHlavuOcaso(ocas,hlava,posledniPozice):
    XH = hlava['X']
    YH = hlava['Y']
    XO = ocas['X']
    YO = ocas['Y']

    if(abs(abs(XH) - abs(XO)) > 1 or abs(abs(YH) - abs(YO)) > 1):
        ocas['X'] = posledniPozice['X']
        ocas['Y']  = posledniPozice['Y']
        poziceXY = "pozice:x:" + str(posledniPozice['X']) + ':y:' + str(posledniPozice['Y'])
        listPozic.append(poziceXY)
        return



def sumPosunu(kamPosunout,kolik):
    global pocetL 
    global pocetR
    global pocetU
    global pocetD
    if(kamPosunout=="L"):
        pocetL += kolik
        return
    if(kamPosunout=="R"):
        pocetR += kolik
        return
    if(kamPosunout=="U"):
        pocetU += kolik
        return
    if(kamPosunout=="D"):
        pocetD += kolik
    return



for posun in listX:
    tokens = posun.split(' ')
    kamPosunout = tokens[0]
    okolik = int(tokens[1].strip())
    sumPosunu(kamPosunout,okolik)
    for c in range(okolik):
        if(kamPosunout == "U"):
            aktualPoziceHlava['Y'] = aktualPoziceHlava['Y'] + 1


        if(kamPosunout == "D" ):
            aktualPoziceHlava['Y'] = aktualPoziceHlava['Y'] - 1

        
        if(kamPosunout == "L"):
            aktualPoziceHlava['X'] = aktualPoziceHlava['X'] - 1 
             

        if(kamPosunout == "R"):
            aktualPoziceHlava['X'] = aktualPoziceHlava['X'] + 1

        porovnejHlavuOcaso(aktualPoziceOcas,aktualPoziceHlava,tempPozice)
        tempPozice['X'] = aktualPoziceHlava['X'] 
        tempPozice['Y'] = aktualPoziceHlava['Y'] 


print("celkem pozic: " + str(len(listPozic)+1))


listPozic = list(dict.fromkeys(listPozic))
print("celkem pozic bez duplicit: " + str(len(listPozic)+1))


print('L:' + str(pocetL))
print('R:' + str(pocetR))
print('U:' + str(pocetU))
print('D:' + str(pocetD))



#první pokus = 6402 byl špatně, your answer is too high
#druhý pokus = 462 byl špatně, your answer is too low
#třetí pokus = 6385 byl špatně,your answer is too high
#čtvrtý pokus = 6324 byl špatně
#pátý pokus = 6325 byl špatně