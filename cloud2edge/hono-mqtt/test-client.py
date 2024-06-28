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

# Define callback functions (optional)
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
    else:
        print(f"Connection failed with code {rc}")

def on_publish(client, userdata, mid):
    print("Message published")

# Assign the callback functions
client.on_connect = on_connect
client.on_publish = on_publish

# Connect to the broker
client.connect(broker_address, port)

# Start the loop
client.loop_start()

# Function to generate a random value
def get_random_value():
    return random.randint(0, 100)

try:
    while True:
        # Create a message with a random value
        message = {
            "topic": "org.acme/my-device-1/things/twin/commands/modify",
            "headers": {},
            "path": "/features/temperature/properties/value",
            "value": get_random_value()
        }

        # Convert message to JSON format
        message_json = json.dumps(message)

        # Publish the message
        result = client.publish(topic, message_json)

        # Wait for the message to be published
        # result.wait_for_publish()

        # Print feedback
        print(f"Published message: {message_json}")

        # Wait for a while before publishing the next message
        time.sleep(1)  # Adjust the delay as needed

except KeyboardInterrupt:
    print("\nDisconnecting from broker...")
    # Disconnect from the broker
    client.disconnect()
    # Stop the loop
    client.loop_stop()
