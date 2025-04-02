import math

def perimetre_cercle(rayon):
    if int(rayon)>0:
        return 2*math.pi*int(rayon)
    else:
        print("Merci de rentrer un nombre positif!")
        return -1

mon_rayon = input("Rayon du cercle : ")
perimetre = perimetre_cercle(mon_rayon)
print("Perimètre du cercle = ", perimetre)
