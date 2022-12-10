
with open("02data.txt") as data:
    lines = data.readlines()


#A = kámen(1 bod) => já = X(kámen)
#B = papír(2 body) => já = Y(papír)
#C = nuzky(3 body) => já = Z(nuzky)
# prohra = 0, nerozhodně = 3, výhra = 6
#výhra je kdyz on dá A a já Y = bodům 2(papír) + 6(váhra) = 8
#výhra je kdyz on dá B a já Z = bodům 3(nuzky) + 6(váhra) = 9
#výhra je kdyz on dá C a já X = bodům 1(kamen) + 6(váhra) = 7

#situace k 2. části úkolu:A Y,   B X,  C Z
# X = prohra
# Y = remíza
# Z = výhra




situaceA1 ="A X" #kámen prohra = nuzky 3 + 0 = 3
situaceA2 ="A Y" #kámen remiza = kamen 1 + 3 = 4
situaceA3 ="A Z" #kámen vyhra = papir 2 + 6 = 8

situaceB1 ="B X" #papír prohra = kámen 1 + 0 = 1
situaceB2 ="B Y" #papír remiza = papír 2 + 3 = 5
situaceB3 ="B Z" #papír vyhra = nuzky 3 + 6 = 9

situaceC1 ="C X" #nuzky prohra = papir 2 + 0 = 2
situaceC2 ="C Y" #nuzky remiza = nuzky 3 + 3 = 6
situaceC3 ="C Z" #nuzky vyhra = kamen 1 + 6 = 7

celkemBodu = 0
for l in lines:
    bod = 0
    if(situaceA1 in l):
        bod = 3
    if(situaceA2 in l):
        bod = 4
    if(situaceA3 in l):
        bod = 8
    if(situaceB1 in l):
        bod = 1
    if(situaceB2 in l):
        bod = 5
    if(situaceB3 in l):
        bod = 9
    if(situaceC1 in l):
        bod = 2
    if(situaceC2 in l):
        bod = 6
    if(situaceC3 in l):
        bod = 7

    celkemBodu += bod



print(celkemBodu)

    #tokens = l.split(' ')
    #on = tokens[0]
    #ja =tokens[1].strip()
    #if(on=="A"):
    #   if(ja=="X")