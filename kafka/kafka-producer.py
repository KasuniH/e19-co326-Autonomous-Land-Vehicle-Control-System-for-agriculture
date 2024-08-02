from confluent_kafka import Producer
import socket

# Kafka broker
broker = '10.96.190.31:9094'

# Kafka topic
topic = 'ditto-msg'

# Create Producer instance
p = Producer({
    'bootstrap.servers': broker,
    'client.id': socket.gethostname(),
    'receive.message.max.bytes': 2000000000  # Increase this value as needed
})

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

# Produce a message
message = "Hello, Kafka!"
p.produce(topic, message.encode('utf-8'), callback=delivery_report)

# Wait up to 1 second for events. Callbacks will be invoked during
# this method call if the message is acknowledged.
p.poll(1)

# Wait for any outstanding messages to be delivered and delivery reports
# to be received.
p.flush()
