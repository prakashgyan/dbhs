#!/bin/sh
source .venv/bin/activate
python -m flask --app src.app run -p $PORT --debug