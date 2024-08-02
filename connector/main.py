import json
import paho.mqtt.client as mqtt

class Vehicle:
    def __init__(self):
        self.soil_temperature = 0
        self.soil_moisture = 0
        self.locationX = 0
        self.locationY = 0
        self.soil_ph = 0
        self.air_temperature = 0
        self.air_humidity = 0
        self.vehicle_id = ""

def create_data(vehicle):
    data = {
        "soil-temperature": vehicle.soil_temperature,
        "soil-moisture": vehicle.soil_moisture,
        "locationX": vehicle.locationX,
        "locationY": vehicle.locationY,
        "soil-ph": vehicle.soil_ph,
        "air-temperature": vehicle.air_temperature,
        "air-humidity": vehicle.air_humidity,
        "vehicle_id": vehicle.vehicle_id
    }
    return data

vehicle_arr = []

for i in range(1, 4):
    vehicle = Vehicle()
    vehicle.vehicle_id = f"vehicle-{i}"
    vehicle_arr.append(vehicle)

# Define the MQTT broker details
broker_address = "test.mosquitto.org"
port = 1883

# Define the topic to subscribe to
topic = "opentwins/#"

# Define the MQTT client
client = mqtt.Client()

# Define callback functions
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        # Subscribe to the topic upon successful connection
        client.subscribe(topic)
        print(f"Subscribed to topic: {topic}")
    else:
        print(f"Connection failed with code {rc}")

def on_message(client, userdata, msg):
    # Convert the received message payload to a JSON object
    try:
        message_json = json.loads(msg.payload.decode())
    except json.JSONDecodeError as e:
        print(f"Failed to decode message payload as JSON: {e}")
        return

    if 'path' not in message_json or 'value' not in message_json:
        # print("Invalid message format")
        return

    vehicle_id = msg.topic.split('/')[-1]
    feature = message_json['path'].split('/')[2]
    value = message_json['value']

    vehicle = None
    for i in vehicle_arr:
        if i.vehicle_id == vehicle_id:
            vehicle = i
            break

    if vehicle is None:
        print(f"Vehicle with ID {vehicle_id} not found")
        return

    if feature == "soil-temperature":
        vehicle.soil_temperature = value
    elif feature == "soil-moisture":
        vehicle.soil_moisture = value
    elif feature == "locationX":
        vehicle.locationX = value
    elif feature == "locationY":
        vehicle.locationY = value
    elif feature == "soil-ph":
        vehicle.soil_ph = value
    elif feature == "air-temperature":
        vehicle.air_temperature = value
    elif feature == "air-humidity":
        vehicle.air_humidity = value
    
    data = create_data(vehicle)

    json_data = json.dumps(data)

    client.publish("opentwins", json_data)
    
    print(data)   

# Assign the callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
client.connect(broker_address, port)

# Start the loop
client.loop_forever()
