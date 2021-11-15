# https://docs.python.org/fr/3.8/library/importlib.html#importlib.import_module

import os
import json
import logging
import importlib
import tempfile
import requests
import importlib.util
import pathlib
import subprocess
from urllib import request
import app.software_ui.window as sui_windows

def run_app():
    """Same as name Run App

        launch process:
            - `check_version`
            - `sui_windows.Windows_interface`
            - `generate_url`
            - `downloader`
    """

    # start Logger
    save_path = directory()
    logging.basicConfig( filename=save_path + 'wc.log',
                        level=logging.DEBUG,
      format='%(asctime)s -- %(filename)s -- %(lineno)d -\
- %(name)s -- %(levelname)s -- %(message)s')

    check_version()# TODO a faire dans un futur proche

    url_dict = {}

    # launch windows_interface
    sotfware_list = sui_windows.Windows_interface().result_list_to_return


    if len(sotfware_list) < 1:
        exit()

    software_path:str = None

    for software in sotfware_list:
        try:
            #  convert software liste to liste software/url
            url_dict[software] = generate_url(software)
            file_name = url_dict[software]
            logging.debug(f"convert in url {software} into {file_name}")
        except:
            logging.error(f"impossible de resoudre l'url de -> {software}")

        # TEST: a controler
        # name = software_distant_name_resolver(url_dict[software])
        # print("name ",name)
#        try:
#             # récuprération du nom du fichier
#             url = url_dict[software]
#             logging.debug(f"url avant recuperation du nom {url}")
#             file_name = request.urlopen(
#                 request.Request(url)).info().get_filename()

#             logging.info(f"récupération du nom de fichier sur le dossier distant :\
# { file_name }")
#        except:
#            logging.error("impossible de récuéperer le nom du file")
        try:
            # Download file from URL
            software_path = download(url_dict[software]) #FIXME: Activate downloader
            logging.debug(f"Téchargement du fichier -> {software_path}")
        except:
            logging.error("impossible de download le file")

    # lance l'installation
    logging.debug(f"file_name -> {file_name}")

    install_download_app( software_path)


def software_distant_name_resolver(url):
    logging.debug(f"Enter in software distant name resolver -> {url}")
    file_name:str = ""

    # récuprération du nom du fichier
    file_name = request.urlopen(request.Request(url)).info().get_filename()
    logging.debug(f"récupération du nom de fichier sur le dossier distant : \
{ file_name }")

    return file_name


def check_version(): #TODO fonction futur a finir
    """Check on distant repository if version as same
    """

    # recuperation sur github du hash du dernier commit
    # et comparaison

    # FIXME:
    # a voir si on garde, code fonctionnel
    # pour injecter la liste des softwares dans une
    # variable en passant par un fichier tmp detruit juste après

    # make tmpfile
    with tempfile.TemporaryFile() as fp:
        temp = tempfile.NamedTemporaryFile(prefix='wc_', suffix='.json')
        url = 'http://dev.johnben.fr/software.json'
        r = requests.get(url, allow_redirects=True)
        open(temp.name, 'wb').write(r.content)
        software_list = r.content
        f = open(temp.name)
        data = json.load(f)
        f.close()
        software_list = json.dumps(tuple(dict(data)))


def generate_url(soft_name):
    """Start Url creation from list sofware

        start import dynamically from liste Pattern
        and start make_url form module Software

        ARGS: str : name of software

        RETURN: str: URL to download software

    """
    logging.debug(f"Enter in generate url -> { soft_name }")

    try:
        module = import_lib(soft_name)
        logging.debug(f"sortie Creation import lib -> { module }")
        return module.make_url()
    except:
        logging.error(f"Software Libary -> {soft_name} not found")


def import_lib(soft_name):
    """Dynamicaly Load Import

        Load dynamically lib
        software_model $software_name

        ARGS: str software_name

        RETURN: none lib is charged
    """
    logging.debug(f"Enter in import Lib -> { soft_name }")

    # get cureent directory
    current_path = os.getcwd()

    logging.debug(f"current_path -> {current_path}")
    # make temp path for import
    spec = importlib.util.spec_from_file_location("alias" ,
            f"{current_path}/app/software_model/software_{soft_name}.py")

    module_to_import = importlib.util.module_from_spec(spec)

    # import path
    spec.loader.exec_module(module_to_import)
    return module_to_import


def software_name_extractor(software_url):
    """Extract Name from URL

    Args:
        software_url (string): url of the software
    """

    logging.debug(f"Entre in software name extractor -> {software_url}")

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
    logging.debug(f"Enter in download -> { software_url } ")

    software_name = software_name_extractor(software_url)

    # Make object for download file
    downloaded_obj = requests.get(software_url)

    # Make path for save the file
    save_path = directory()
    complete_save_path = os.path.join(save_path, software_name)

    # check if file exist
    if not os.path.isfile(complete_save_path):
        with open( complete_save_path, "wb") as file:
            # écriture du fichier dans abs_path
            file.write(downloaded_obj.content)
            file.close()
        # Control si le fichier est déjà present
            logging.warn(f"File -> {software_name} doesn't exist, downloaded")
    #return the software path for instal module

    logging.debug(f"adresse retour complete_save_path -> { complete_save_path }")
    return complete_save_path


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

#         test = input(f"Le dossier {folder} n'éxiste pas!\
# Voulez vous le créer ? (yes/no) " )
#         if test == "yes":
#             p = pathlib.Path(save_path)
#             p.mkdir(parents=True, exist_ok=True)
#         elif test == "no":
#             logging.warning("Annulé.")
#             pass
#         else:
#             logging.warning("Mauvais Choix !")
#             exit()

            p = pathlib.Path(save_path)
            p.mkdir(parents=True, exist_ok=True)
    return save_path


def install_download_app( software_path):
    logging.debug(f"Enter in install download app  ->{software_path}")

    # Split name for extract extension
    software_extension = os.path.splitext(software_path)
    logging.debug(f" split path & get extension  -> {software_extension[1]}")

    if software_extension[1] == ".pkg":
        logging.debug(f"file is ->pkg")
        subprocess .call(
            f"installer -pkg {software_path} -target /",
            shell =True)

    elif software_extension[1] == ".dmg":
        logging.debug(f"file is ->dmg")
        ...

    elif software_extension[1] == ".bzip":
        logging.debug(f"file is ->bzip")
        ...

    elif software_extension[1] == ".tar":
        logging.debug(f"file is ->tar")
        ...

    elif software_extension[1] == ".json":
        logging.debug(f"file is ->json")
        subprocess .call(f"open -a TextEdit {software_path}", shell =True)
    else:
        logging.debug(f"unknow file")
        print("Extension non reconnu")


if __name__ == "__main__":
    os.system("clear")


    # TODO: gestion erreur manque logiciel
