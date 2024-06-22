from confluent_kafka import Consumer, KafkaError

# Kafka broker settings
bootstrap_servers = '35.225.173.80:8090'  # Use the broker address without 'ssl://'

# Kafka topics to consume from
topics = [
    '_/_/things/live/commands',
    '_/_/things/live/messages',
    '_/_/things/twin/events',
    '_/_/things/live/events'
]

# Kafka consumer configuration
conf = {
    'bootstrap.servers': bootstrap_servers,
    'group.id': 'my-consumer-group',  # Specify a consumer group ID
    'auto.offset.reset': 'earliest',  # Start consuming from the beginning of the topic
    'security.protocol': 'SASL_SSL',
    'ssl.ca.location': 'kafka.crt',  # Replace with the path to your CA certificate file
    'sasl.mechanism': 'PLAIN',
    'sasl.username': 'ditto-c2e',  # Replace with your SASL username
    'sasl.password': 'verysecret',  # Replace with your SASL password
}

# Create a Kafka consumer
consumer = Consumer(conf)

# Subscribe to the topics
consumer.subscribe(topics)

try:
    while True:
        # Poll for messages
        msg = consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            # Handle errors
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # End of partition
                print(f"Reached end of partition {msg.topic()} [{msg.partition()}]")
            elif msg.error():
                # Other errors
                print(f"Error occurred: {msg.error()}")
        else:
            # Print the received message
            print(f"Received message: {msg.value().decode('utf-8')} from topic {msg.topic()} partition [{msg.partition()}] offset {msg.offset()}")

except KeyboardInterrupt:
    pass

finally:
    # Close the consumer
    consumer.close()
