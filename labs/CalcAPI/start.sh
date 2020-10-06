#!/bin/bash
exec gunicorn -c gu.conf application
