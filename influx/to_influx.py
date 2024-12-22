import pandas as pd
from influxdb_client import InfluxDBClient, Point, WriteOptions
from influxdb_client.client.write_api import ASYNCHRONOUS
from concurrent.futures import ThreadPoolExecutor

# Load the dataset
df = pd.read_csv('data2.csv')

# InfluxDB configuration
bucket = "Robot"
org = "UOP"
token = "ZwwKNMjWScg-4_1ofFDCIKO8jSjRGm4M3sx6KkdeWq7OiKBXXL3cWrfiec0lp6unZTrXaaNvY8JSMqAX_ZU3UQ=="
url = "http://localhost:8086"

# Create an InfluxDB client
client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=WriteOptions(batch_size=10000, flush_interval=10000, write_type=ASYNCHRONOUS))

def write_batch(start, end):
    points = []
    for index, row in df.iloc[start:end].iterrows():
        point = Point("data") \
            .field("soil_moisture", row["soil_moisture"]) \
            .field("temperature", row["temperature"]) \
            .field("soil_humidity", row["soil_humidity"]) \
            .field("air_temperature", row["air_temperature"])
        points.append(point)
    write_api.write(bucket=bucket, org=org, record=points)

# Use ThreadPoolExecutor to write data in parallel
batch_size = 10000
num_batches = (len(df) + batch_size - 1) // batch_size  # Calculate the number of batches
with ThreadPoolExecutor(max_workers=4) as executor:  # Adjust max_workers based on your system
    for i in range(num_batches):
        start = i * batch_size
        end = min(start + batch_size, len(df))
        executor.submit(write_batch, start, end)

# Ensure all data is written
write_api.flush()
client.close()
