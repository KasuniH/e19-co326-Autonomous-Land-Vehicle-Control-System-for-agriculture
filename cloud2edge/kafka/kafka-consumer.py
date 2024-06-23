from confluent_kafka import Consumer, KafkaException, KafkaError

# Kafka broker
broker = '184.73.139.235:8082'
# Kafka topic
topic = 'ditto-msg'
# Consumer group
group = 'my-group'

# Create Consumer instance
c = Consumer({
    'bootstrap.servers': broker,
    'group.id': group,
    'auto.offset.reset': 'earliest',
    'receive.message.max.bytes': 2000000000  # Increase this value as needed
})

# Subscribe to topic
c.subscribe([topic])

def consume_loop(consumer, topics):
    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    print('%% %s [%d] reached end at offset %d\n' %
                          (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                print('Received message: {}'.format(msg.value().decode('utf-8')))
    finally:
        # Close down consumer to commit final offsets.
        consumer.close()

consume_loop(c, [topic])
