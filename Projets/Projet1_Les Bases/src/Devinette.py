import random

nombre = random.randint(1,20)

devine = int(input("A quelle nombre je pense entre 1 et 20 ? : "))

while nombre != devine:
    if devine > nombre:
        print("C'est plus petit")
    else:
        print("C'est plus grand")
    devine = int(input("Une autre idée : "))

print("Bravo, tu as trouvé, c'était bien " + str(nombre))
