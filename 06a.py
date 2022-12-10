#kolik znaků musím zpracovat než mám za sebou 4 jdoucí písmena různorodá?
#bvwbj plbgvbhsrlpgdmjqwftvncz = 5

with open("06data.txt") as data:
    listX = data.readline()

pozice=0
for c in listX:
    string4char = listX[pozice:pozice+4]
    tempList = []
    tempList.extend(string4char)
    jak = (len(tempList) != len(set(tempList)))
    if( jak == False):
        print("koza")
        print(pozice + 4)
        break

    pozice +=1

# výsledek 1100 byl dobře na poprvé
# doba řešení 20 minut