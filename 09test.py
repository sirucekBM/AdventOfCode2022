with open("data\\09data.txt") as data:
    listX = data.readlines()



ocas = {'X':0,'Y':0}
hlava = {'X':0,'Y':0}
tempPozice = {'X':0,'Y':0}
listPozic=[]
poziceXY = "pozice:x:" + str(0) + ':y:' + str(0)
listPozic.append(poziceXY)

for posun in listX:
    tokens = posun.split(' ')
    kamPosunout = tokens[0]
    okolik = int(tokens[1].strip())
    for c in range(okolik):
        if(kamPosunout == "U"):
            hlava['Y'] = hlava['Y'] + 1


        if(kamPosunout == "D" ):
            hlava['Y'] = hlava['Y'] - 1

        
        if(kamPosunout == "L"):
            hlava['X'] = hlava['X'] - 1 
             

        if(kamPosunout == "R"):
            hlava['X'] = hlava['X'] + 1



        if(abs(abs(hlava['X'] ) - abs(ocas['X'])) > 1 or abs(abs(hlava['Y'] ) - abs(ocas['Y'])) > 1):
            ocas['X'] = tempPozice['X']
            ocas['Y']  = tempPozice['Y']
            poziceXY = "pozice:x:" + str(tempPozice['X']) + ':y:' + str(tempPozice['Y'])
            listPozic.append(poziceXY)


        tempPozice['X'] = hlava['X'] 
        tempPozice['Y'] = hlava['Y']             



print("celkem pozic: " + str(len(listPozic)))
listPozic = list(dict.fromkeys(listPozic))
print("celkem pozic bez duplicit: " + str(len(listPozic)))


#první pokus = 6402 byl špatně, your answer is too high
#druhý pokus = 462 byl špatně, your answer is too low
#třetí pokus = 6385 byl špatně,your answer is too high
#čtvrtý pokus = 6324 byl špatně
#pátý pokus = 6325 byl špatně