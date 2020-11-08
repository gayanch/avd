#!/bin/sh
source appenv/bin/activate
uwsgi --ini avd.ini 1>>/app/log/avd.log 2>>/app/log/avd_error.log