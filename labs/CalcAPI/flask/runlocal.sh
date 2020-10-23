#!/bin/bash

make cleanall
./calctest
chmod +x pytest.py
./pytest.py

mkdir ./flaskapp
cp ./flask/requirements.txt ./flaskapp
cp ./flask/rungunicorn.sh ./flaskapp
cp ./flask/application.py ./flaskapp
cp ./flask/gu.local ./flaskapp/gu.py

python3 -m venv ./flaskapp
cp -r ./pycalc ./flaskapp/lib/python3.6/site-packages/
cp -r ./bin ./flaskapp

cd flaskapp
source bin/activate
pip3 install -r requirements.txt
deactivate

chmod +x rungunicorn.sh
./rungunicorn.sh
