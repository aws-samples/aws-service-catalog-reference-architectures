#!/bin/bash
exec gunicorn -c gu.py application
