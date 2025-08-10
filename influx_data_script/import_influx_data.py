import influxdb_client, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from influx_db_secrets import INFLUX_DB_TOKEN, INFLUX_DB_IP, INFLUX_DB_ORG

write_client = None

def start_influx_client():
    global write_client
    write_client = influxdb_client.InfluxDBClient(url=INFLUX_DB_IP, token=INFLUX_DB_TOKEN, org=INFLUX_DB_ORG)

def test_write_data():
    bucket="tfm"
    global write_client

    write_api = write_client.write_api(write_options=SYNCHRONOUS)
    
    for value in range(5):
        point = (
            Point("measurement1")
            .tag("tagname1", "tagvalue1")
            .field("field1", value)
        )
        write_api.write(bucket=bucket, org="tfm", record=point)
        time.sleep(1) # separate points by 1 second

if __name__ == "__main__":
    start_influx_client()
    test_write_data()