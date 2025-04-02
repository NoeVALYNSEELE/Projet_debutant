class Unite: # Création de la classe Unite
    def __init__(self): # Initialisation de la classe
        self.length_units = { # Définition des unités de longueur (dictionnaire)
            "m" : 1,
            "cm": 0.01,
            "km" :1000,
            "mm" : 0.001
        }
        self.weight_units = { # Définition des unités de poids (dictionnaire)
            "g":1,
            "kg":1000
        }
    
    def convert_length(self, value, from_unit, to_unit): # Méthode pour convertir les unités de longueur
         if from_unit in self.length_units and to_unit in self.length_units: # Vérifie si les unités de départ et d'arrivée sont valides (présentes dans le dictionnaire)
             base_value = value*self.length_units[from_unit] # Conversion de la valeur de départ en unité de base (mètre)
             converted_value = base_value/self.length_units[to_unit] # Conversion de l'unité de base en unité d'arrivée
             return converted_value # Retourne la valeur convertie
         else:
             raise ValueError("Unités de longueur invalides") # Retourne une erreur si les unités ne sont pas valides
         
    def convert_weight(self, value, from_unit, to_unit): # Méthode pour convertir les unités de poids
        if from_unit in self.weight_units and to_unit in self.weight_units:
            base_value = value * self.weight_units[from_unit]
            converted_value = base_value / self.weight_units[to_unit]
            return converted_value
        else:
            raise ValueError("Unités de poids invalides")
        
def main(): # Fonction principale
        converter = Unite() # Création d'une instance de la classe Unite (pour accéder aux méthodes de conversion de la classe)
        while True: # Boucle infini pour afficher le menu et traiter les choix de l'utilisateur
            print("Convertisseur d'unités de Noé")
            print("1. Longueur")
            print("2. Poids")
            print("3. Quitter")
            choice = input("Choisissez une option : ").strip() # Demande à l'utilisateur de choisir une option + suppression des espaces inutiles en début et fin de la chaîne (strip)

            if choice == "1": # Si l'utilisateur choisit l'option 1 (Longueur)
                value = float(input("Entrez la valeur à convertir :")) # Demande à l'utilisateur de saisir la valeur à convertir 
                from_unit = input("Entrez l'unité de départ (m, km, cm,mm) : ").strip() # Demande à l'utilisateur de saisir l'unité de départ + suppression des espaces inutiles
                to_unit = input("Entrez l'unité souhaitée (m, km, cm, mm) : ").strip() # Demande à l'utilisateur de saisir l'unité d'arrivée + suppression des espaces inutiles
                try:
                    result = converter.convert_length(value, from_unit, to_unit) # Appel de la méthode de conversion de la classe Unite
                    print(f"{value} {from_unit} = {result} {to_unit}") # Affichage du résultat de la conversion 
                except ValueError as e: # Gestion des erreurs
                    print(e) # Affichage du message d'erreur

            elif choice == "2":
                value = float(input("Entrez la valeur à convertir :"))
                from_unit = input("Entrez l'unité de départ (g, kg) : ").strip()
                to_unit = input("Entrez l'unité souhaitée (g, kg) : ").strip()
                try:
                    result = converter.convert_weight(value, from_unit, to_unit)
                    print(f"{value} {from_unit} = {result} {to_unit}")
                except ValueError as e:
                    print(e)

            elif choice == "3":
                print("Au revoir!")
                break # Sortie de la boucle infinie

            else:
                print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__": # Si le fichier est exécuté directement (pas importé en tant que module)
        main() # Appel de la fonction principale