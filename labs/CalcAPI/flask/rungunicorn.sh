#!/bin/bash
source bin/activate
exec bin/gunicorn -c gu.py application:app
deactivate
