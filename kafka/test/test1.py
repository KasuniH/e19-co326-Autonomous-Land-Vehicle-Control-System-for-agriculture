from confluent_kafka import Consumer, KafkaException

topic = 'ditto-topic'

# Configuration for the Kafka consumer
config = {
    'bootstrap.servers': 'pkc-12576z.us-west2.gcp.confluent.cloud:9092',  # Your Kafka broker endpoint
    'security.protocol': 'SASL_SSL',
    'sasl.mechanism': 'PLAIN',
    'sasl.username': '2IE7RVDBKBR2L7R3',
    'sasl.password': 'kyHb0HnV2ZG8PCKUoT6LFrXhZZqKC9PyF/4bV4ezQ4/yvmObk6a8V5MimTQ1LNWL',
    'group.id': 'my-consumer-group',
    'auto.offset.reset': 'earliest'
}

# Create a Kafka consumer
consumer = Consumer(config)
consumer.subscribe([topic])

# Polling loop
try:
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # End of partition
                continue
            elif msg.error():
                raise KafkaException(msg.error())
        else:
            print(f"Received message: {msg.key().decode('utf-8')} {msg.value().decode('utf-8')}")
except KeyboardInterrupt:
    pass
finally:
    consumer.close()
