# https://docs.python.org/fr/3.8/library/importlib.html#importlib.import_module

import os
import logging
import importlib
import tempfile
import requests
import importlib.util
import pathlib
import app.software_ui.window as sui_windows


def generate_url(soft_name):
    """Start Url creation from list sofware

        start import dynamically from liste Pattern
        and start make_url form module Software

        ARGS: str : name of software

        RETURN: str: URL to download software

    """

    try:
        print("trie imprt lib")
        module = import_lib(soft_name)
        print("module.make_url()",module.make_url())
        return module.make_url()
    except:
        print(f"Software Libary {soft_name} not found")


def import_lib(soft_name):
    """Dynamicaly Load Import

        Load dynamically lib
        software_model $software_name

        ARGS: str software_name

        RETURN: none lib is charged
    """
    print("enter imprt lib")

    current_patch = os.getcwd()
    spec = importlib.util.spec_from_file_location("alias" , f"{current_patch}/app/software_model/software_{soft_name}.py")
    module_to_import = importlib.util.module_from_spec(spec)

    spec.loader.exec_module(module_to_import)
    print("module_to_import",module_to_import)
    return module_to_import


def software_name_extractor(software_url):
    """Extrct Name from URL

    Args:
        software_url (string): url of the software
    """
    # Split Url for extract extesion
    software_name = os.path.splitext(software_url)

    #save Extension
    software_extension = software_name[1]

    #split for extract name
    software_name_splited = software_name[0].split("/")

    # lenght of the list
    software_len = len(software_name_splited)

    #take the last elements
    software_name = software_name_splited[software_len -1]
    # return join name whit .ext
    return software_name + software_extension


def download(software_url):
    """Download file from remote

    Args:
        url (string): name folder to save
        complete_save_path : Abs path ex:/Users/titi/download/
        file_name : real file name - license.txt

    Return:
        File
    """

    software_name = software_name_extractor(software_url)

    print("65 enter in download ---->", software_name, software_url)

    # Make object for download file
    downloaded_obj = requests.get(software_url)

    # Make patch for save the file
    save_path = directory()
    complete_save_path = os.path.join(save_path, software_name)

    # check if file exist
    if not os.path.isfile(complete_save_path):
        with open( complete_save_path, "wb") as file:
            # écriture du fichier dans abs_path
            file.write(downloaded_obj.content)
            file.close()
        # Control si le fichier est déjà present
            print(" - ", software_name, "Téléchargement ok")
    else:
        print(" - ", software_name, " déjà Téléchargé")


def directory()-> str:
    """return the absolute path to save the files    """

    # current_path = os.getcwd()
    current_path = os.path.expanduser('~')
    folder = "wc"

    # Path pour l'enregistrement du fichier
    save_path = current_path + "/" + folder + "/"

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

# def start_app():
#     """Download all the applications entered in the Application_list"""

#     save_path = directory()

#     # Parcours des listes de nom et adresse par valeur


#     #name = lst[0] # TEST
#     file_name = "license.txt"
#     url = "https://johnben.ch/"

#     complete_save_path = os.path.join(save_path, file_name)

#     #TODO: integrer une regle regex pour le nom de fichier
#     processing(url,complete_save_path,file_name)



def check_version(): #TODO
    """Check on distant repository if version as same
    """
    import json

    with tempfile.TemporaryFile() as fp:
        temp = tempfile.NamedTemporaryFile(prefix='wc_', suffix='.json')
        url = 'http://dev.johnben.fr/software.json'
        r = requests.get(url, allow_redirects=True)
        open(temp.name, 'wb').write(r.content)
        software_list = r.content
        f = open(temp.name)
        data = json.load(f)
        f.close()
        print(tuple(data.items()))
        software_list = json.dumps(tuple(dict(data)))
        print("software_list",software_list)

    # complete_url = os.path.join(url, file_name)
    # downloaded_obj = requests.get(complete_url)

    # if not os.path.isfile(complete_save_path):
    #     with open( complete_save_path, "wb") as file:
    #         # écriture du fichier dans abs_path
    #         file.write(downloaded_obj.content)
    #         file.close()

    #     # Control si le fichier est déjà present
    #         print(" - ", file_name, "Téléchargement ok")
    # else:
    #     print(" - ", file_name, " déjà Téléchargé")

def run_app():
    """Same as name Run App

        launch process:
            - `check_version`
            - `sui_windows.Windows_interface`
            - `generate_url`
            - `downloader`
    """

    # charge le Logger
    logging.basicConfig(filename='myapp.log', level=logging.INFO,\
      format='%(asctime)s -- %(filename)s -- %(lineno)d -- %(name)s -- %(levelname)s -- %(message)s')

    logging.info(" check Version application from Github")
    check_version()
    logging.info("version Checked")

    url_dict = {}

    # launch windows_interface
    sotfware_list = sui_windows.Windows_interface().result_list_to_return

#TEST:
    if len(sotfware_list) > 1:
        print("118 sotfware_list en retour",sotfware_list)
    else:
        print("vide")

    # #  convert software liste to liste software/url
    for software in sotfware_list:
        try:
            url_dict[software] = generate_url(software)
            try:
                # Download file from URL
                download(url_dict[software])
            except:
                logging.error("Impossible de telecharger l'url")
        except:
            logging.error(f"impossible de resoudre l'url de {software}")


    # lance l'installation
if __name__ == "__main__":
    os.system("clear")


    # TODO: gestion erreur manque logiciel
