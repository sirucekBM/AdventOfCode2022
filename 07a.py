# Najděte všechny adresáře s celkovou velikostí maximálně 100 000.
# Jaký je součet celkových velikostí těchto adresářů?
 
with open("07data.txt") as data:
    listX = data.readlines()
 
"""
with open("07data.txt") as data:
    fp.writelines(L)
    listX = [line for line in data]
"""
 
# adresářů je 153
# souborů je 190
 
#$ ls
#dir czpnrsfc
#načti soubory
listSouboru =[]
for adr in listX:
    if('dir' not in adr and '$' not in adr):
        listSouboru.append(adr.strip())
 
listSouboru = list(dict.fromkeys(listSouboru))
print("počet souborů: " + str(len(listSouboru)))
 
#načti jména adresářů
listAdresaru =[]
for adr in listX:
    if('dir' in adr):
        adresar  = adr.strip()
        adresar = adresar.replace('dir', '').strip()
        listAdresaru.append(adresar)
 
listAdresaru = list(dict.fromkeys(listAdresaru))
#listAdresaru.sort()
print("počet adresářů: " +str(len(listAdresaru)))#'wqcsrw' 'jllhmmf'
 
#----------vytvořím si slovník adresářů------------
slovnikAdresaru ={}
for ad in listAdresaru:
    slovnikAdresaru[ad] = seznamSouboru =[]
 
#---------do slovníku naházím soubory a složky------------------------------------------
# takže klíč je složka a hodnota je list všeho, co je v této složce (soubory, složky)
nalezenAdresar = False
zacatekVypisu = False
for adr in listX:
    if('$ cd ..' in adr):
        nalezenAdresar = False
        zacatekVypisu = False
        continue
 
    if('$ cd' in adr and  '$ cd /' not in adr):
        aktualAdresar = adr.strip()
        aktualAdresar = aktualAdresar.replace('$ cd ','').strip()
        nalezenAdresar = True
        continue
 
    if(nalezenAdresar):
        if(adr.strip()=='$ ls'):
            zacatekVypisu = True
            continue
   
    if(zacatekVypisu):
        slovnikAdresaru[aktualAdresar].append(adr.strip())


#-----------------------------------------------------------------------
# příklad položky ve slovníku:  'gddqh':['dir cfvpq', '318413 jrfpjdpw.znd', 'dir wwv']
# tuto složku nelze zahrnou do výpočtu, neb obsahuje soubor, který je vetší než 100 000
#-----------------------------------------------------------------------

#----------najdu si složky, které obsahují pouze soubory a žádné další složky---------
slozkyPouzeSeSoubory={}
countA = 0
counter = 0
for key, value in slovnikAdresaru.items():
    counter +=1
    celkemVelikost = 0
    for itemX in value:
        if('dir ' not in itemX):
            tokens = itemX.split(' ')
            velikost = int(tokens[0])
            celkemVelikost += velikost
        else:
            countA += 1
            continue

        if(celkemVelikost>0):
            slozkyPouzeSeSoubory[key]=celkemVelikost

print("počet všech adresářů: " + str(counter))
print("počet adresářů, jenž obsahují pouze soubory: " + str(len(slozkyPouzeSeSoubory.keys())))
print("počet adresářů, jenž obsahují i složky: " + str(countA))
#-----------------------------------------------------------------------------
#-------------sečtu složky, které patří do výběru--------------
#-----------JSOU TO COR SLOŽKY, KTERÉ NEOBSAHUJÍ UŽ DALŠÍ SLOŽKU---------
#--------------součet těchto složek je část výsledného součtu----------------
slovnikNevyhovujicichAdresaru = {}
slovnikVyhovujicichAdresaru = {}
sumaVyhovujicichAdresaru = 0
for key, value in slozkyPouzeSeSoubory.items():
    if(value > 100000):
        slovnikNevyhovujicichAdresaru[key] ="x"
    else:
        slovnikVyhovujicichAdresaru[key] =value
        sumaVyhovujicichAdresaru += value


print("počet adresářů, jenž nevyhovují: " + str(len(slovnikNevyhovujicichAdresaru.keys())))
print("počet adresářů, jenž vyhovují: " + str(len(slovnikVyhovujicichAdresaru.keys())))
print("celková suma cor adresářů: " +str(sumaVyhovujicichAdresaru))

#------------vytvořím slovník ze zbytku-----------------
slovnikBezCorSlozek ={}
for key, value in slovnikAdresaru.items():
    if (key in slovnikVyhovujicichAdresaru):
        continue
    slovnikBezCorSlozek[key]= value
#--------------------------------------------------------

slovnikBezCorSlozekUpraveny ={}
for key, value in slovnikBezCorSlozek.items():
    slovnikBezCorSlozekUpraveny[key] = vel =[0]
    for itemX in value:
        if('dir' not in itemX):#pokud je to soubor
            tokens = itemX.split(' ')
            velikost = int(tokens[0])
            slovnikBezCorSlozekUpraveny[key].append(velikost)
        else:#je to adresář
            tempAdr = itemX .replace('dir ','').strip()
            if (tempAdr in slovnikVyhovujicichAdresaru):
                tempV = slovnikVyhovujicichAdresaru[tempAdr]
                slovnikBezCorSlozekUpraveny[key].append(tempV)
            else:
                if (tempAdr in slovnikNevyhovujicichAdresaru):
                    slovnikBezCorSlozekUpraveny[key].append(1000000)
                else:
                    slovnikBezCorSlozekUpraveny[key].append(itemX)

#---------------------tady pokračovat---------------------------------


#---------------- ze slovnikAdresaru vytvořím slovník vypočtených hodnot------
slovnikAdresaruPouzeKumulHodnoty ={}
for key, value in slovnikAdresaru.items():
    if (key in slovnikNevyhovujicichAdresaru):
        continue
    slovnikAdresaruPouzeKumulHodnoty[key] = vel =[0]
    for itemX in value:
        if('dir' not in itemX):#pokud je to soubor
            tokens = itemX.split(' ')
            velikost = int(tokens[0])
            slovnikAdresaruPouzeKumulHodnoty[key].append(velikost)
        else:#je to adresář
            tempAdr = itemX .replace('dir ','').strip()
            if (tempAdr in slovnikVyhovujicichAdresaru):
                velikost = slovnikVyhovujicichAdresaru[tempAdr]
                slovnikAdresaruPouzeKumulHodnoty[key].append(velikost)
                continue
            else:
                continue

#------------------------------------------------------------------------
vyslednaSuma = 0
for key, value in slovnikAdresaruPouzeKumulHodnoty.items():
    if (key in slovnikVyhovujicichAdresaru):
        continue
    tempSuma = 0
    for itemX in value:
        tempSuma += itemX
    if(tempSuma<=100000):
        vyslednaSuma += tempSuma
print("=====================================")
print("============FINÁLE===============")
print("výsledná suma: " + str(vyslednaSuma))
print("výsledná  kumul suma: " + str(vyslednaSuma + sumaVyhovujicichAdresaru))
print("=====================================")


#první pokus = 1 477 570 byl špatně => too low
#druhý pokus = 2 705 491 byl špatně => too high
#třetí pokus = 1 702 008 byl špatně => too low
#1702008
#suma adresářů bez podsložek = 1 260 944