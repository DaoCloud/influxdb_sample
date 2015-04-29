# influxdb_sample
Run an application on DaoCloud platform. This application will draw sine line into the influxdb database.

##Build Image
docker build -t daocloud/influxdb-sample

##Use docker link primitives in influxdb-sample's ENV

###web console port ENV

INFLUXDB_PORT
INFLUXDB_PORT_8083_TCP_ADDR
INFLUXDB_PORT_8083_TCP
INFLUXDB_PORT_8083_TCP_PROTO
INFLUXDB_PORT_8083_TCP_PORT

###https port ENV
INFLUXDB_PORT_8084_TCP_ADDR
INFLUXDB_PORT_8084_TCP
INFLUXDB_PORT_8084_TCP_PROTO
INFLUXDB_PORT_8084_TCP_PORT

###http port env
INFLUXDB_PORT_8086_TCP_ADDR
INFLUXDB_PORT_8086_TCP
INFLUXDB_PORT_8086_TCP_PROTO
INFLUXDB_PORT_8086_TCP_PORT
INFLUXDB_PASSWORD
INFLUXDB_USERNAME

###In influxdb-sample, get env like this to contact with influxdb
host = os.getenv('INFLUXDB_PORT_8086_TCP_ADDR')
port = os.getenv('INFLUXDB_PORT_8086_TCP_PORT')
user = os.getenv('INFLUXDB_USERNAME')
password = os.getenv('INFLUXDB_PASSWORD')
url = 'http://%s:%s/db?u=%s&p=%s'%(host, port, user, password)


