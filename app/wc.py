# https://docs.python.org/fr/3.8/library/importlib.html#importlib.import_module

import importlib
import importlib.util
import logging
import os
import pathlib
from tkinter.constants import NONE
from urllib import request
import requests

import ssl
# Pour eviter Échec de la vérification du certificat :
ssl._create_default_https_context = ssl._create_unverified_context


import app.software_ui.window as sui_windows
from app.extension_strategy import InstallationStrategy
from app.extension_strategy import NAME_STRATEGY_MAPPING

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

    url_dict = {}

    # launch windows_interface
    sotfware_list = sui_windows.Windows_interface().result_list_to_return


    if len(sotfware_list) < 1:
        exit()

    software_path: str = ""
    file_name:str = ""

    for software in sotfware_list:
        try:
            #  convert software liste to liste software/url
            url_dict[software] = generate_url(software)
            file_name = url_dict[software]
            logging.debug(f"convert in url {software} into {file_name}")
        except:
            logging.error(f"impossible de resoudre l'url de -> {software}")


        try:
            # Download file from URL
            logging.debug(f"Téchargement du fichier -> {software_path}")
            software_path = download(url_dict[software]) #FIXME: Activate downloader
        except:
            logging.error("impossible de download le file")

        # lance l'installation
        logging.debug(f"===>Enter in install download app  ->{software_path}")

        # Split name for extract extension


        install_download_app(software_path)




def software_distant_name_resolver(url):
    """Extract Name from URL

    Args:
        software_url (string): url of the software
    """
    logging.debug(f"===>Enter in software distant name resolver -> {url}")
    # récuprération du nom du fichier

    logging.debug(f"software name extractor 1-> {url}")
    logging.debug(f"url avant recuperation du nom {url}")
    software_name = request.urlopen(
        request.Request(url)).info().get_filename()

    logging.info(f"software name extractor 1 :{ software_name }")
    if not software_name == None:
        return software_name

    elif software_name == None:
        logging.debug(f"software name extractor 2-> {url}")

        # Split Url for extract extesion
        software_name = os.path.splitext(url)

        #save Extension
        software_extension = software_name[1]

        #split for extract name
        software_name_splited = software_name[0].split("/")

        # lenght of the list
        software_len = len(software_name_splited)

        #take the last elements
        software_name = software_name_splited[software_len -1]
        # return join name whit .ext
        logging.debug(f"Extension {software_name}{software_extension}")
        return software_name + software_extension
    else:
        logging.error("impossible de récuéperer le nom du file")



def generate_url(soft_name):
    """Start Url creation from list sofware

        start import dynamically from liste Pattern
        and start make_url form module Software

        ARGS: str : name of software

        RETURN: str: URL to download software

    """
    logging.debug(f"===>Enter in generate url -> { soft_name }")

    module = import_lib(soft_name)
    logging.debug(f"sortie Creation import lib -> { module }")
    return module.make_url()
    try:
        ...
    except:
        logging.error(f"Software Libary -> {soft_name} not found")


def import_lib(soft_name):
    """Dynamicaly Load Import

        Load dynamically lib
        software_model $software_name

        ARGS: str software_name

        RETURN: none lib is charged
    """
    logging.debug(f"===>Enter in import Lib -> { soft_name }")

    # get cureent directory
    current_path = os.getcwd()

    logging.debug(f"current_path -> {current_path}")
    # make temp path for import
    spec = importlib.util.spec_from_file_location("alias" ,
            f"{current_path}/app/software_model/software_{soft_name}.py")

    logging.debug(f"Control addr import: \
{current_path}/app/software_model/software_{soft_name}.py")
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
    logging.debug(f"===>Enter in download -> { software_url } ")

    software_name = software_distant_name_resolver(software_url)


    # Make path for save the file
    save_path = directory()
    complete_save_path = os.path.join(save_path, software_name)
    logging.debug(f"path to save before dl {save_path}{software_name}")
    # check if file exist
    logging.debug(f"Control software {os.path.isfile(complete_save_path)}")
    if not os.path.isfile(complete_save_path):
        print("not exist")
        # Make object for download file
        downloaded_obj = requests.get(software_url)
        with open( complete_save_path, "wb") as file:
            logging.warn(f"File -> {software_name} doesn't exist, downloaded")
            # écriture du fichier dans abs_path
            file.write(downloaded_obj.content)
            file.close()
    else:
        logging.warn(f"File -> {software_name} exist, not downloaded")
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
    if not os.path.isdir(save_path):
        p = pathlib.Path(save_path)
        p.mkdir(parents=True, exist_ok=True)
    return save_path


def install_download_app( software_path:str):
    """Install application with Strategy

    Args:
        software_path (str): path abs of each application
        strategy (InstallationStrategy): abstract Class
    """
    logging.debug(f"===>Enter in install download app  ->{software_path}")

    # Split name for extract extension

    software_extension = os.path.splitext(software_path)
    logging.debug(f" split path & get extension  -> {software_extension[1]}")

    strategy = NAME_STRATEGY_MAPPING[software_extension[1]]

    strategy.execute(software_path)#TODO: var path & name


if __name__ == "__main__":
    os.system("clear")


    # TODO: gestion erreur manque logiciel
