from confluent_kafka import Consumer, KafkaException

# Configuration for the Kafka consumer
config = {
    'bootstrap.servers': '34.42.82.181:9092',  # Your Kafka broker endpoint
    'group.id': 'my-group',                    # Consumer group id
    'auto.offset.reset': 'earliest',           # Start reading from the earliest message
}

# Create a Kafka consumer
consumer = Consumer(config)

# Subscribe to the topic
topic = 'ditto-topic'
consumer.subscribe([topic])

def consume_messages():
    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaException._PARTITION_EOF:
                    # End of partition event
                    print(f"Reached end of partition: {msg.partition()}")
                else:
                    print(f"Consumer error: {msg.error()}")
                continue
            print(f"Consumed message from {msg.topic()} [{msg.partition()}] at offset {msg.offset()}: key={msg.key()}, value={msg.value()}")
    except KeyboardInterrupt:
        print("Aborted by user")
    finally:
        # Close the consumer
        consumer.close()

if __name__ == "__main__":
    consume_messages()
