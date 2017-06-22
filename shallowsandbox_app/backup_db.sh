#!/bin/bash

# Backup the current production database to the ci server
DATE=`date +%Y-%m-%d_%H:%M:%S`
scp /home/gabe/shallowsandbox/shallowsandbox/shallowsandbox_app/shallowsandbox.db gabe@104.236.170.47:/home/gabe/db_backups/shallowsandbox/shallowsandbox-$DATE.db
