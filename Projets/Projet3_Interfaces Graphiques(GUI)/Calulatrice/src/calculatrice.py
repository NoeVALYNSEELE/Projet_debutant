import sys #importation du module sys qui fournit un accès à certaines variables utilisées ou maintenues par l'interpréteur et à des fonctions qui interagissent fortement avec l'interpréteur.
from PyQt6 import uic, QtWidgets  #importation des classes uic et QtWidgets de PyQt6
from PyQt6.QtWidgets import QApplication, QMainWindow #importation des classes QApplication et QMainWindow de PyQt6.QtWidgets

class Calculatrice(QMainWindow): #classe de la calculatrice (modèle ou un plan qui définit les propriétés (attributs) et les comportements (méthodes) que les objets créés à partir de cette classe peuvent avoir. Une classe permet de créer des objets qui partagent les mêmes caractéristiques et comportements.)
    def __init__(self): #initialisation de la classe
        super().__init__() 
        uic.loadUi("C:\\Users\\noeva\\OneDrive\\Bureau\\Python\\Interface Graphique\\Calulatrice\\calculator.ui", self)  # chargement de l'interface dans la fenêtre principale
        #définition les actions des boutons
        self.bouton_0.clicked.connect(lambda: self.append_number("0")) #quant le bouton 0 est cliqué, on ajoute 0 à l'écran via la fonction append_number + lambda pour passer un argument (0)
        self.bouton_1.clicked.connect(lambda: self.append_number("1"))
        self.bouton_2.clicked.connect(lambda: self.append_number("2"))
        self.bouton_3.clicked.connect(lambda: self.append_number("3"))
        self.bouton_4.clicked.connect(lambda: self.append_number("4"))
        self.bouton_5.clicked.connect(lambda: self.append_number("5"))
        self.bouton_6.clicked.connect(lambda: self.append_number("6"))
        self.bouton_7.clicked.connect(lambda: self.append_number("7"))
        self.bouton_8.clicked.connect(lambda: self.append_number("8"))
        self.bouton_9.clicked.connect(lambda: self.append_number("9"))
        self.bouton_plus.clicked.connect(lambda: self.append_operator("+"))
        self.bouton_moins.clicked.connect(lambda: self.append_operator("-"))
        self.bouton_fois.clicked.connect(lambda: self.append_operator("*"))
        self.bouton_divise.clicked.connect(lambda: self.append_operator("/"))
        self.bouton_egal.clicked.connect(self.calculate_result)
        self.bouton_clear.clicked.connect(self.clear_display)
        self.bouton_virgule.clicked.connect(lambda: self.append_decimal())

    def append_number(self, number): #ajout d'un chiffre à l'écran
        current_text = self.display.text() #récupération du texte actuel
        new_text = current_text + number #ajout du chiffre
        self.display.setText(new_text) #mise à jour de l'écran

    def append_operator(self, operator): #ajout d'un opérateur à l'écran
        current_text = self.display.text()
        new_text = current_text + " " + operator + " "
        self.display.setText(new_text)

    def append_decimal(self): #ajout d'une virgule à l'écran
        current_text = self.display.text()
        if not current_text.endswith("."): #vérification si le dernier caractère n'est pas déjà une virgule
            new_text = current_text + "."
            self.display.setText(new_text)

    def calculate_result(self):
        try: 
            result = eval(self.display.text()) #calcul de l'expression (eval permet d'évaluer une expression mathématique et de l'effectuer)
            self.display.setText(str(result)) #affichage du résultat
        except Exception as e: #si une erreur survient
            self.display.setText("Erreur") #affichage du message d'erreur

    def clear_display(self): #effacement de l'écran
        self.display.clear()


# lancement de l'application
if __name__ == "__main__": #si le fichier est exécuté directement
    app = QtWidgets.QApplication(sys.argv) #création de l'application
    window = Calculatrice() #création de la fenêtre
    window.show() #affichage de la fenêtre
    sys.exit(app.exec()) #exécution de l'application