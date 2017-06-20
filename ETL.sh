#!/bin/sh
set -e
python prepare_data.py $1 #Extract and transformation job
hive -f LoadnQuery.hql    #Loading into database

