#!/bin/bash

cd ../
make cleanall
./calctest
./pytest.py

cd flask/
mkdir ~/flaskapp
cp requirements.txt ~/flaskapp
cp rungunicorn.sh ~/flaskapp
cp application.py ~/flaskapp
cp gu.local ~/flaskapp/gu.conf

virtualenv ~/flaskapp
cp -R ../pycalc/ ~/flaskapp/lib/python2.7/site-packages/
cp ../bin/* ~/flaskapp/bin/

cd ~/flaskapp
source bin/activate
pip install -r requirements.txt
deactivate

./rungunicorn.sh
