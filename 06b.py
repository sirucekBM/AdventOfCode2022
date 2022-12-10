#kolik znaků musím zpracovat než mám za sebou 14 jdoucí písmena různorodá?
#bvwbj plbgvbhsrlpgdmjqwftvncz = 5

#mjq jpqmgbljsphdztnv jfqwrcgsmlb: první značka za znakem 19
#bvwbj plbgvbhsrlpgdmjqwf tvncz: první značka za znakem 23



with open("06data.txt") as data:
    listX = data.readline()

pozice=0
for c in listX:
    string14char = listX[pozice:pozice+14]
    tempList = []
    tempList.extend(string14char)
    jak = (len(tempList) != len(set(tempList)))
    if( jak == False):
        print("koza")
        print(pozice + 14)
        break

    pozice +=1


    #první pokus = 2411 nebyl dobře (too low)  , druhý pokus = 2421 byl dobře
    #doba 10 minut