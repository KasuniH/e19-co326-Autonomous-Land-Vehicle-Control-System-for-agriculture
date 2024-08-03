from kafka import KafkaConsumer
import json

# Configuration for the Kafka consumer
consumer = KafkaConsumer(
    'opentwins',
    bootstrap_servers=['34.42.82.181:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

def consume_messages():
    try:
        for message in consumer:
            data = message.value
            print(f"Consumed message from {message.topic} [{message.partition}] at offset {message.offset}: {data}")
    except KeyboardInterrupt:
        print("Aborted by user")
    finally:
        consumer.close()

if __name__ == "__main__":
    consume_messages()
