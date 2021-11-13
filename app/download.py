import requests
import os
import pathlib

def processing(url,complete_save_path,file_name):
    """ get a file using url.

        Keyword arguments:
            url : LICENSE - name folder to save
            complete_save_path : Abs path ex:/Users/titi/download/
            file_name : real file name - license.txt"""

    complete_url = os.path.join(url, file_name)
    downloaded_obj = requests.get(complete_url)

    if not os.path.isfile(complete_save_path):
        with open( complete_save_path, "wb") as file:
            # écriture du fichier dans abs_path
            file.write(downloaded_obj.content)
            file.close()

        # Control si le fichier est déjà present
            print(" - ", file_name, "Téléchargement ok")
    else:
        print(" - ", file_name, " déjà Téléchargé")

def directory()-> str:
    """return the absolute path to save the files    """

    current_path = os.getcwd()
    folder = "download"

    # Path pour l'enregistrement du fichier
    save_path = current_path + "/telechargement_app/" + folder + "/"

    # Check si dossier deja creer
    #FIXME: trouver la validation if exist ou un truc du genre
    if not os.path.isdir(save_path):
        test = input(f"Le dossier {folder} n'éxiste pas!\
Voulez vous le créer ? (yes/no) " )
        if test == "yes":
            p = pathlib.Path(save_path)
            p.mkdir(parents=True, exist_ok=True)
        elif test == "no":
            print("Annulé.")
            pass
        else:
            print("Mauvais Choix !")
            exit()
    return save_path

def start_app():
    """Download all the applications entered in the Application_list"""

    save_path = directory()

    # Parcours des listes de nom et adresse par valeur
    for lst in app_list.Application_liste : # lst est la valeur

        #name = lst[0] # TEST
        file_name = lst[1] # license.txt
        url = lst[2] # https://johnben.ch/

        complete_save_path = os.path.join(save_path, file_name)

        #TODO: integrer une regle regex pour le nom de fichier
        processing(url,complete_save_path,file_name)