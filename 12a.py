import collections

with open("data\\12data.txt") as data:
    listX = data.readlines()

#tady si jen pro info načtu do slovníku písmena-----------
slovnikBodu={}
for r in listX:
    for p in r:
        if(len(p.strip())<1):
            continue
        if p in slovnikBodu:           
            slovnikBodu[p]=slovnikBodu[p] + 1
        else:
            slovnikBodu[p]=1
od = collections.OrderedDict(sorted(slovnikBodu.items()))
print('k')
#---------------------------------------------------------