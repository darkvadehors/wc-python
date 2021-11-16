
#!/bin/sh

chmod +x py2app_install.sh

$APPLICATION_NAME="wc"
CURRENT_PATH=$PWD
echo "changement de dossier"
cd $CURRENT_PATH

conda install -c conda-forge py2app
conda install -c conda-forge/label/cf202003 py2app
echo "py2app installé"
py2applet --make-setup wc
rm -rf build dist
echo "build et dist supprime"
python setup.py py2app -A
echo "Alias créé"
echo "lancement de l'application"
./dist/wc.app/Contents/MacOS/wc


