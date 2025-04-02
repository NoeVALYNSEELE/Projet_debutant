import json # module pour la gestion des fichiers JSON(sauvegarde long terme des données)
from PyQt6 import uic #importation de la classe uic de PyQt6
from PyQt6.QtWidgets import QApplication, QMainWindow #importation des classes QApplication et QMainWindow de PyQt6.QtWidgets
from PyQt6.QtGui import QColor #importation de la classe QColor de PyQt6.QtGui

class ToDoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"C:\Users\noeva\OneDrive\Bureau\Python\Interface Graphique\To-Do Liste\todo_list.ui", self)  # chargement de l'interface dans la fenêtre principale
        self.load_tasks() #chargement des tâches sauvegardées
        #définition les actions des boutons
        self.button_add.clicked.connect(self.add_task) 
        self.button_delete.clicked.connect(self.delete_task)
        self.button_done.clicked.connect(self.mark_task_done)
        QApplication.instance().aboutToQuit.connect(self.save_tasks) #sauvegarde des tâches avant la fermeture de l'application

    def add_task(self): #ajout d'une tâche
        task = self.input_task.text() #récupération de la tâche saisie
        if task: #si la tâche n'est pas vide
            self.task_list.addItem(task)  #ajout de la tâche à la liste
            self.input_task.clear() #effacement de la zone de saisie

    def delete_task(self): #suppression d'une tâche
        selected_item = self.task_list.currentItem() #récupération de l'élément sélectionné
        if selected_item:
            self.task_list.takeItem(self.task_list.row(selected_item)) #suppression de l'élément
    
    def mark_task_done(self): #marquage d'une tâche comme terminée
        selected_item = self.task_list.currentItem() #récupération de l'élément sélectionné
        if selected_item:
            selected_item.setForeground(QColor("green")) #modification de la couleur de l'élément en vert
    
    def save_tasks(self): #sauvegarde des tâches
        tasks = [self.task_list.item(i).text() for i in range(self.task_list.count())] #récupération de toutes les tâches
        with open("tasks.json", "w") as f: #ouverture du fichier en écriture
            json.dump(tasks, f) #sauvegarde des tâches

    def load_tasks(self): #chargement des tâches sauvegardées
        try:
            with open("tasks.json", "r") as f: #ouverture du fichier en lecture
                tasks = json.load(f) #chargement des tâches
                self.task_list.addItems(tasks) #ajout des tâches à la liste
        except FileNotFoundError:
            pass
        
# lancement de l'application
app = QApplication([]) #création de l'application
window = ToDoApp() #création de la fenêtre
window.show() #affichage de la fenêtre
app.exec() #exécution de l'application  