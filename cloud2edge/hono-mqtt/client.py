import paho.mqtt.client as mqtt

# Define the MQTT broker details
broker_address = "test.mosquitto.org"
port = 1883

# Define the topic to subscribe to
topic = "co326/#"

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
    # Print received message
    print(f"Received message from topic {msg.topic}:\n {msg.payload.decode()}")

# Assign the callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
client.connect(broker_address, port)

# Start the loop
client.loop_forever()
