import json
from kafka import KafkaProducer

# Create a producer with JSON serializer
producer = KafkaProducer(
    bootstrap_servers='10.96.190.31:9094',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def on_send_success(record_metadata):
    print(record_metadata.topic)
    print(record_metadata.partition)
    print(record_metadata.offset)

def on_send_error(excp):
    print('I am an errback', exc_info=excp)

# Sending a message with callbacks
producer.send('my_topic', b'some_message_bytes').add_callback(on_send_success).add_errback(on_send_error)