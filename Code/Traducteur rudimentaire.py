anglais = {"bonjour" : "hello", "chien" : "dog", "chat" : "cat", "chante" : "sing", "maison" : "house"}

mot = input("Quel mot voulez vous traduire (bonjour, chien, chat, chante, maison) : ")

if mot in anglais :
    print(mot + " se dit " + anglais[mot] + " en anglais.")
else:
    print("Désolée, je ne connais pas ce mot :(")
