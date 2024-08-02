import time
import json
import random
from kafka.producer import KafkaProducer


def random_temp_cels():
    return round(random.uniform(-10, 50), 1)

def random_humidity():
    return round(random.uniform(0, 100), 1)

def random_voltage():
    return round(random.uniform(110, 240), 1)

def random_current():
    return round(random.uniform(0, 30), 1)

def get_json_data(floor):
    data = {
        "floor": floor,
        "temperature": random_temp_cels(),
        "humidity": random_humidity(),
        "voltage": random_voltage(),
        "current": random_current()
    }
    return json.dumps(data)

def main():
    producer = KafkaProducer(
        bootstrap_servers=['pkc-12576z.us-west2.gcp.confluent.cloud:9092'],
        security_protocol='SASL_SSL',
        sasl_mechanism='PLAIN',
        sasl_plain_username='2IE7RVDBKBR2L7R3',  # Replace with your Confluent Cloud API key
        sasl_plain_password='kyHb0HnV2ZG8PCKUoT6LFrXhZZqKC9PyF/4bV4ezQ4/yvmObk6a8V5MimTQ1LNWL',  # Replace with your Confluent Cloud API secret
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    floors = ["Floor1", "Floor2", "Floor3"]

    print(100)

    for _ in range(20000):
        for floor in floors:
            json_data = get_json_data(floor)
            producer.send('ditto-topic', value=json_data)
            print(f"Sensor data sent for {floor}: {json_data}")
        time.sleep(5)

if __name__ == "__main__":
    main()
