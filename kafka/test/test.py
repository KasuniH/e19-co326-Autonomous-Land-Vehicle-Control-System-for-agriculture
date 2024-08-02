import time
from confluent_kafka import Producer

topic = 'ditto-topic'


# Configuration for the Kafka producer
config = {
    'bootstrap.servers': 'pkc-12576z.us-west2.gcp.confluent.cloud:9092',  # Your Kafka broker endpoint
    'security.protocol': 'SASL_SSL',
    'sasl.mechanism': 'PLAIN',
    'sasl.username': "2IE7RVDBKBR2L7R3",
    'sasl.password': "kyHb0HnV2ZG8PCKUoT6LFrXhZZqKC9PyF/4bV4ezQ4/yvmObk6a8V5MimTQ1LNWL"
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
    producer.produce(topic, key=key, value=value, callback=delivery_report)
    producer.flush()

if __name__ == "__main__":
    # Example message
    # loop
    while True:
        produce_message(key="key1", value="Hello, Kafka!")
        time.sleep(1)