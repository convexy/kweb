#!/usr/bin/bash
sudo apt -y update
sudo apt -y dist-upgrade
sudo apt -y autoremove

sudo apt -y install python3 python-is-python3 sqlite3

python -m venv .
source bin/activate
python -m pip install -r requirements.txt
