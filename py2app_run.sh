#!/bin/sh


CURRENT_PATH=$PWD
echo "changement de dossier"
cd $CURRENT_PATH

rm -rf build dist
echo "build et dist supprime"
python3 setup.py py2app -A
echo "Alias créé"
echo "lancement de l'aaplication"
/dist/wc.app/Contents/MacOS/wc.app


