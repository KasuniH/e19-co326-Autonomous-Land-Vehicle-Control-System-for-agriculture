import time
import json
import random
import paho.mqtt.client as mqtt

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

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

def on_publish(client, userdata, mid):
    print(f"Message {mid} published")

def main():
    # MQTT broker settings
    broker = 'test.mosquitto.org'
    port = 1883
    topic = 'opentwins'

    # Create MQTT client
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_publish = on_publish

    # Connect to the broker
    client.connect(broker, port, 60)
    client.loop_start()

    floors = ["Floor1", "Floor2", "Floor3"]

    for _ in range(20000):
        for floor in floors:
            json_data = get_json_data(floor)
            client.publish(topic, json_data)
            print(f"Sensor data sent for {floor}: {json_data}")
        time.sleep(1)

    client.loop_stop()
    client.disconnect()

if __name__ == "__main__":
    main()
