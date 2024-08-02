import ssl
import paho.mqtt.client as mqtt
import json
import random
import time

# Define the MQTT broker details
broker_address = "34.71.8.184"
port = 8883
username = "my-auth-id-1@my-tenant"
password = "my-password"
topic = "telemetry"
ca_cert = "./ca.crt"

# Define the MQTT client
client = mqtt.Client()

# Set the username and password for the client
client.username_pw_set(username, password)

# Configure TLS/SSL settings
client.tls_set(ca_cert, certfile=None, keyfile=None, tls_version=ssl.PROTOCOL_TLS, ciphers=None)
client.tls_insecure_set(True)

# Define the topic to subscribe to
topic = "org.acme/#"

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
