import survival


listSurvivor = []
listAGe = []

def iterable(listItem,listAppend):

    for item in listItem:
        
        listAppend.append(item/100.0)


iterable(survival.listSurvival,listSurvivor)
print len(listSurvivor)
print listSurvivor

iterable(survival.listaAgeAttack,listAGe)
print len(listAGe)
print listAGe



