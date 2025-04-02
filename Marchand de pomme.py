nombre=int(input("Combien de pommes? : "))

if nombre == 1:
    print("Voici votre pomme")
elif nombre>2 and nombre<10:
    print("Voici vos " + str(nombre) + " pomme")
else:
    print("Je n'ai plus de pomme")
