#!/bin/bash

/usr/bin/python3 scel2txt.py
cp out/*.dict.yaml /home/donspace/.config/ibus/rime/
cd /home/donspace/wordlib/
/usr/bin/python3 cplib.py