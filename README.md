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
# TP_git_Emie_Suhayl
TROISIEME PARTIE 

linux@Linux:~/Documents/TP_git_Emie_Suhayl$ git log
commit 7cb708a78a4a42746bb1b469d539d98dadb1ea7d (HEAD -> main, bdd)
Author: Votre Nom <mapulcherie@student.udm.ac.mu>
Date:   Thu Mar 7 19:06:06 2024 +0400

    nouvelle fonction ajouter au fichier JSON

commit ef85b6dac461dd83bcccd04d22ce1c1b74dd6d22 (origin/bdd)
Author: Linux <linux@Linux.myguest.virtualbox.org>
Date:   Thu Mar 7 13:20:08 2024 +0400

    charger un fichier Json

commit 048ddc08f1951b6d5ffd957356f546d19ab2b5b0
Author: Linux <linux@Linux.myguest.virtualbox.org>
Date:   Thu Mar 7 13:12:30 2024 +0400

    prend un dictionnaire

commit 23785599d75879639637f57802aff7511079d87d (origin/main, origin/HEAD)
Author: EmiePul <162488686+EmiePul@users.noreply.github.com>
Date:   Thu Mar 7 10:50:00 2024 +0400

    Initial commit
linux@Linux:~/Documents/TP_git_Em

D'apres linux les commits ont bien ete fait mais je n'arrive pas a sauvegarder ce commits sur le main a cause d'une erreur d'authentication dont je ne trouve pas la solution

def main():
    print("Que souhaitez-vous faire ?")
    print("1. Charger une liste de tâches")
    print("2. Créer une liste de tâches")

    choice = input("Entrez votre choix (1 ou 2) : ")

    if choice == "1":
        load_tasks()
    elif choice == "2":
        create_tasks()
    else:
        print("Choix invalide. Veuillez entrer 1 ou 2.")

def load_tasks():
    print("Chargement de la liste de tâches...")
    # Ajouter le code pour charger une liste de tâches

def create_tasks():
    print("Création d'une nouvelle liste de tâches...")
    # Ajouter le code pour créer une liste de tâches

if __name__ == "__main__":
    main()
