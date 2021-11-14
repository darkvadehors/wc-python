#!/bin/sh

$APPLICATION_NAME="wc"
CURRENT_PATH=$PWD
echo "changement de dossier"
cd $CURRENT_PATH

conda install -c conda-forge py2app
conda install -c conda-forge/label/cf202003 py2app
echo "py2app installé"
py2applet --make-setup $APPLICATION_NAME
rm -rf build dist
echo "build et dist supprime"
python setup.py py2app -A
echo "Alias créé"
echo "lancement de l'aaplication"
./dist/$APPLICATION_NAME.app/Contents/MacOS/$APPLICATION_NAME


