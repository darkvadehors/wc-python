import abc
import subprocess
import logging
import os
import zipfile
import app.wc



class InstallationStrategy( abc.ABC ):
    @classmethod
    @abc.abstractmethod
    def execute(cls):
        """Abstract Methode definign the rules for all extension type"""
        print("Class abstract")

class PkgInstallationStrategy( InstallationStrategy ):
    @classmethod
    def execute(cls , software_path ):
        logging.debug(f"file is ->pkg")
        subprocess .call(
            f"sudo -S installer -allowUntrusted -verbose -pkg {software_path} -target /",
            shell =True)

        return super().execute()

class DmgInstallationStrategy( InstallationStrategy ):
    @classmethod
    def execute(cls, software_path):
        logging.debug(f"file is ->Dmg")
        subprocess .call(f"sudo hdiutil attach {software_path}")
        for file in os.listdir("/mydir"):
            if file.endswith(".app"):
                print(os.path.join("/mydir", file))
                # os.replace(software_path, "path/to/new/destination/for/file.foo")

        return super().execute()

class BzipInstallationStrategy( InstallationStrategy ):
    @classmethod
    def execute(cls, software_path):
        logging.debug(f"file is ->Bzip")
        return super().execute()

class TarInstallationStrategy( InstallationStrategy ):
    @classmethod
    def execute(cls, software_path):
        logging.debug(f"file is ->Tar")
        return super().execute()

class ZipInstallationStrategy( InstallationStrategy ):
    @classmethod
    def execute(cls, software_path):
        logging.debug(f"file is ->Zip")

        # importing required modules
        from zipfile import ZipFile

        # specifying the zip file name
        file_name = software_path
        name = app.wc.software_distant_name_resolver(software_path)

        # opening the zip file in READ mode
        with ZipFile(file_name, 'r') as zip:

            # extracting all the files

            zip.extractall(os.path.expanduser('~/wc/'))
            zip.write(name)


        return super().execute()

NAME_STRATEGY_MAPPING = {
    ".dmg" : DmgInstallationStrategy,
    ".pkg" : PkgInstallationStrategy,
    ".tar" : TarInstallationStrategy,
    ".bzip" : BzipInstallationStrategy,
    ".zip" : ZipInstallationStrategy,
}

def install_download_app(soft_path: str, strategy: InstallationStrategy):
    strategy.execute(soft_path)

if __name__ == "__main__":
    # on cherche a isoler notre extension bla bla
    extension = ".pkg"
    strategy = NAME_STRATEGY_MAPPING[extension]

    # install_download_app( "blabla/blibli" , strategy)




#     """



# Tout d'abord, montez l'image dmg : sudo hdiutil attach <image>.dmg

# L'image sera montée sur /Volumes/<image>. Le mien contenait un paquet que j'ai installé avec : sudo installer -package /Volumes/<image>/<image>.pkg -target /

# Enfin démonter l'image : sudo hdiutil detach /Volumes/<image>.






# script complet



#     # usage: installdmg https://example.com/path/to/pkg.dmg
# function installdmg {
#     set -x
#     tempd=$(mktemp -d)
#     curl $1 > $tempd/pkg.dmg
#     listing=$(sudo hdiutil attach $tempd/pkg.dmg | grep Volumes)
#     volume=$(echo "$listing" | cut -f 3)
#     if [ -e "$volume"/*.app ]; then
#       sudo cp -rf "$volume"/*.app /Applications
#     elif [ -e "$volume"/*.pkg ]; then
#       package=$(ls -1 "$volume" | grep .pkg | head -1)
#       sudo installer -pkg "$volume"/"$package" -target /
#     fi
#     sudo hdiutil detach "$(echo "$listing" | cut -f 1)"
#     rm -rf $tempd
#     set +x
# }

















#     """