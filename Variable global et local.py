toto = 0

def ma_fonction():
    #global toto
    toto = 100
    print("Dans ma fonction : " + str(toto))

ma_fonction()
print("Au global : " + str(toto))
