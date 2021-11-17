import os
import re
import logging
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def make_url():
    """ Class model for nmake download url """
    logging.debug("===>Enter in Firefox Module")

    _url_base ="https://download-installer.cdn.mozilla.net/pub/firefox/releases/"
    _remote_software_name = "Firefox"

    # initialize all variables
    lst = []
    version = ["",""]
    ligne = ["",""]

    # remplace space in url
    url = _url_base.replace(" ","%20")# pour supprime les espaces

    req = Request(url)
    a = urlopen(req).read()

    soup = BeautifulSoup(a, 'html.parser')
    x = (soup.find_all('a'))

    for i in x:
        #extract file name and remove / at the end
        file_name = i.extract().get_text().split("/")

        # make list with the first element
        lst = [file_name[0]]

        for row in lst:

            row_split_dot = row.split(".")

            for _ in enumerate(row_split_dot):

                # don't take word
                if row_split_dot[0].isdigit():

                    # regex all caractere a to Z
                    if not re.compile(r"[aZ]").match(row_split_dot[1]):

                        ligne = row_split_dot[:]
                        # don't take version with letter ex:94.0b1
                        if ligne[0] > version[0] and ligne[1].isdigit():
                                version = ligne

    # joint list for come back to a standard version
    software_version = ".".join(version)
    logging.debug(f"Before return {software_version}")
    # Check system version and format url
    if os.uname()[0] == "Darwin":
        return "{}{}/mac/fr/{}%20{}.pkg".format(
            _url_base,
            software_version,
            _remote_software_name,
            software_version,
        )
    elif os.uname()[0] == "Linux":
        architec = os.uname()[1]
        return "{}{}/linux-{}/fr/{}%20{}.tar.bz2".format(
            _url_base,
            software_version,
            architec,
            _remote_software_name,
            software_version,
        )

if __name__ == "__main__":
    os.system("clear")
    print(make_url())