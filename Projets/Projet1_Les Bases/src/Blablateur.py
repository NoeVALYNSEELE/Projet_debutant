import random

qui = ["Noé", "Gabriel", "Anne", "Eric", "Tortipousse"]
quoi = ["rigole","dort","code","court","chante"]
où = ["à Chambéry", "dans ma chambre", "sous la douche", "dans sa voiture"]

while True:
    print(random.choice(qui), random.choice(quoi), random.choice(où) + ".")
    input("Appuyez sur Entrée")

