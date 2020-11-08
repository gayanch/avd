#!/bin/sh
source appenv/bin/activate
uwsgi --ini avd.ini 2>&1 | tee /app/log/avd.log