import time
import json
import random
from kafka import KafkaProducer


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
        "vehicle_id": floor,
        "temperature": random_temp_cels(),
        "humidity": random_humidity(),
        "voltage": random_voltage(),
        "current": random_current()
    }
    return json.dumps(data)

def main():
    producer = KafkaProducer(bootstrap_servers=['34.42.82.181:9092'])

    floors = ["Floor1", "Floor2", "Floor3"]

    for _ in range(20000):
        for floor in floors:
            json_data = get_json_data(floor)
            producer.send('opentwins', value=bytes(json_data, 'utf-8'))
            print(f"Sensor data sent for {floor}: {json_data}")
        time.sleep(5)

if __name__ == "__main__":
    main()
