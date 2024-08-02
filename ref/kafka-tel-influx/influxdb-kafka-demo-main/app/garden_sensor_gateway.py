import time
import json
import random
from confluent_kafka import Producer

# Define the Kafka broker and configuration
KAFKA_BROKER = 'pkc-12576z.us-west2.gcp.confluent.cloud:9092'
KAFKA_TOPIC = 'ditto-topic'

# Kafka configuration
config = {
    'bootstrap.servers': KAFKA_BROKER,
    'security.protocol': 'SASL_SSL',
    'sasl.mechanism': 'PLAIN',
    'sasl.username': '2IE7RVDBKBR2L7R3',
    'sasl.password': 'kyHb0HnV2ZG8PCKUoT6LFrXhZZqKC9PyF/4bV4ezQ4/yvmObk6a8V5MimTQ1LNWL'
}

# Create a Kafka producer
producer = Producer(config)

# Generate random data
def random_temp_cels():
    return round(random.uniform(-10, 50), 1)

def random_humidity():
    return round(random.uniform(0, 100), 1)

def random_wind():
    return round(random.uniform(0, 10), 1)

def random_soil():
    return round(random.uniform(0, 100), 1)

# Create JSON data
def get_json_data():
    data = {
        "temperature": random_temp_cels(),
        "humidity": random_humidity(),
        "wind": random_wind(),
        "soil": random_soil()
    }
    return json.dumps(data)

# Delivery report callback
def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

# Main function
def main():
    try:
        for _ in range(20000):
            json_data = get_json_data()
            producer.produce(KAFKA_TOPIC, value=json_data, callback=delivery_report)
            print(f"Sensor data sent: {json_data}")
            producer.flush()  # Ensure all messages are sent
            time.sleep(5)  # Adjust the interval as needed
    except KeyboardInterrupt:
        pass
    finally:
        producer.close()
        print("Kafka producer closed.")

if __name__ == "__main__":
    main()
