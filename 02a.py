
with open("02data.txt") as data:
    lines = data.readlines()


#A = kámen(1 bod) => já = X(kámen)
#B = papír(2 body) => já = Y(papír)
#C = nuzky(3 body) => já = Z(nuzky)
# prohra = 0, nerozhodně = 3, výhra = 6
#výhra je kdyz on dá A a já Y = bodům 2(papír) + 6(váhra) = 8
#výhra je kdyz on dá B a já Z = bodům 3(nuzky) + 6(váhra) = 9
#výhra je kdyz on dá C a já X = bodům 1(kamen) + 6(váhra) = 7

situaceA1 ="A X" #kámen kámen 1 + 3 = 4
situaceA2 ="A Y" #kámen papír 2 + 6 = 8
situaceA3 ="A Z" #kámen nuzky 3 + 0 = 3

situaceB1 ="B X" #papír kámen 1 + 0 = 1
situaceB2 ="B Y" #papír papír 2 + 3 = 5
situaceB3 ="B Z" #papír nuzky 3 + 6 = 9

situaceC1 ="C X" #nuzky kámen 1 + 6 = 7
situaceC2 ="C Y" #nuzky papír 2 + 0 = 2
situaceC3 ="C Z" #nuzky nuzky 3 + 3 = 6

celkemBodu = 0
for l in lines:
    bod = 0
    if(situaceA1 in l):
        bod = 4
    if(situaceA2 in l):
        bod = 8
    if(situaceA3 in l):
        bod = 3
    if(situaceB1 in l):
        bod = 1
    if(situaceB2 in l):
        bod = 5
    if(situaceB3 in l):
        bod = 9
    if(situaceC1 in l):
        bod = 7
    if(situaceC2 in l):
        bod = 2
    if(situaceC3 in l):
        bod = 6

    celkemBodu += bod



print(celkemBodu)

    #tokens = l.split(' ')
    #on = tokens[0]
    #ja =tokens[1].strip()
    #if(on=="A"):
    #   if(ja=="X")