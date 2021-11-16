#!/bin/sh

echo "Installation des modules ..."


conda create --name nomades_env flask numpy matplotlib

yes | conda install logging
yes | conda install importlib
yes | conda install tempfile
yes | conda install requests
yes | conda install -c anaconda requests
yes | conda install importlib
yes | conda install pathlib
yes | conda install subprocess


conda activate nomades_env
