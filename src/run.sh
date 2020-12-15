#!/bin/bash

# test pdf_parser.py
cd src
ls
python3 pdf_parser.py
ls

# test tesser_api.py
python3 tesser_api.py

## test recognition.py
#export TESSDATA_PREFIX=/src/tessdata/
#python3 recognition.py
#cat __output__.txt

