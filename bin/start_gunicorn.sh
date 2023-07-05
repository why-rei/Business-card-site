#!/bin/bash
source /root/root/oh-no.pw/venv/bin/activate
exec gunicorn  -c "/root/root/oh-no.pw/bcs/gunicorn_config.py" bcs.wsgi
