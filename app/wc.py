# https://docs.python.org/fr/3.8/library/importlib.html#importlib.import_module

import os
import importlib
import importlib.util
import app.software_ui.window as sui_windows
from app.download import start_app

def generate_url(soft_name):
    """Start Url creation from list sofware

        start import dynamically from liste Pattern
        and start make_url form module Software

        ARGS: str : name of software

        RETURN: str: URL to download software

    """
    avancement = "Adresse en construction...."
    print(avancement)

    try:
        module = import_lib(soft_name)
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

    SOFTWARE_PREFIX = "software_"

# COMMENT:
    # path -> module (envie de faire)... mais...
    # il faut faire:
    # path -> intermediaire (spec) -> module
    # donc la t'as preparer ton module pour etre importer, et donc maintenant il faut faire l'import...
    # donc executer une importation l.29

    spec = importlib.util.spec_from_file_location("alias" , f"/Users/johnben/SandBox/-Python/-WC/app/software_model/software_{soft_name}.py")
    module = importlib.util.module_from_spec(spec)

    spec.loader.exec_module(module)
    return module
# COMMENT
    #importlib.import_module('app.software_model')
    #importlib.import_module('software_'+ soft_name)

def download(url):
    folder = start_app(url)


def run_app():

    # sotfware_liste = ["firefox","vscode"]

    url_dict = {}
# launch windows_interface
    # FIXME fenetre HS
    # sotfware_liste = win_ui.main()
    #TEST: recupere les data de la fenetre
    sotfware_list = sui_windows.Windows_interface().result_list_to_return
    print("sotfware_list",sotfware_list)


    #  convert liste software to liste software/url
    for x in sotfware_list:
        try:
            url_dict[x] = generate_url(x)
        except:
            print(f"impossible de resoudre l'url de {x}")


    # lance le telechargement avec l'url





    # [ x for x in list_pattern]




if __name__ == "__main__":
    # pattern = (
    #     {"designer":["firefox","vscode","mamp","AdobeXD","imageoptim","tutu"]},
    #     {"coder":["firefox","vscode","mamp"]}
    #     )

    os.system("clear")
    run_app()



    # TODO: gestion erreur manque logiciel
