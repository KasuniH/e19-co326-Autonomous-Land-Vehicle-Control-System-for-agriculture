import time
from confluent_kafka import Producer

topic = 'ditto-topic'

# Configuration for the Kafka producer
config = {
    'bootstrap.servers': '34.42.82.181:9092',  # Your Kafka broker endpoint
}

# Create a Kafka producer
producer = Producer(config)

# Callback function to confirm message delivery
def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

# Produce a message
def produce_message(key, value):
    try:
        producer.produce(topic, key=key, value=value, callback=delivery_report)
        producer.flush()
    except Exception as e:
        print(f"Failed to produce message: {e}")

if __name__ == "__main__":
    # Example message
    # Loop to produce messages
    while True:
        produce_message(key="key1", value="Hello, Kafka!")
        time.sleep(1)
