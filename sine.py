#!/usr/bin/python
import json
import math
import requests
import sys
import os

from time import sleep

# Read the environment value
host = os.getenv('INFLUXDB_PORT_8086_TCP_ADDR')
if host is None:
    host = "localhost"

port = os.getenv('INFLUXDB_PORT_8086_TCP_PORT')
if port is None:
    port = '8086'

user = os.getenv('INFLUXDB_USERNAME')
if user is None:
    user = 'root'

password = os.getenv('INFLUXDB_PASSWORD')
if password is None:
    password = 'root'


STATUS_MOD = 10
n = 0

# Firstly use the credentials to create an influxdb database.
# We take name db1 as an instance.
db = 'db1'

url = 'http://%s:%s/db?u=%s&p=%s'%(host, port, user, password)
data = {'name': db }

# Start to create influxdb database
r = requests.post( url, data=json.dumps(data))

# Start to to generate points and draw them into influxdb
while True:
    for d in range(0, 360):
        v = [{'name': 'sin', 'columns': ['val'], 'points': [[math.sin(math.radians(d))]]}]
        url = 'http://%s:%s/db/%s/series?u=%s&p=%s'%(host,port,db,user,password)
        r = requests.post(url, data=json.dumps(v))
        if r.status_code != 200:
            print 'Failed to add point to influxdb -- aborting.'
            sys.exit(1)
        n += 1

        sleep(0.01)

        if n % STATUS_MOD == 0:
            print '%d points inserted.' % n