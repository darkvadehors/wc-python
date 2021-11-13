from software import Creation_strategy
from urllib import request
from bs4 import BeautifulSoup
import os

#import requests

class Filezilla( Creation_strategy ):
    """ Class model for nmake download url """

    @classmethod
    def make_url(cls):

        url_base = "https://filezilla-project.org/download.php?platform=osx"

        req = request(url_base)
        a = request.urlopen(req).read()
        soup = BeautifulSoup(a, 'html.parser')
        x = (soup.find_all('a'))
        print(x)



        os_type:str = None
        if os.uname()[0] == "Darwin":
            os_type = "darwin"
        elif os.uname()[0] == "Linux":
            if os.uname()[1] == "debian":
                os_type = "linux-deb-x64"
            elif os.uname()[1] == "Centos" or os.uname()[1] == "RHEL":
                os_type = "linux-rpm-x64"
        else:
            print("Change D'ordinateur")

        return "https://code.visualstudio.com/sha/download?build=stable&os={}-universal".format(
            os_type
        )

            #print("test",[x for x in a for a in lst])
            # try:
            #     float(lst[0])
            #     print("1",lst[0])
            # except:
            #     pass

if __name__ == "__main__":

    print(Vscode.make_url())