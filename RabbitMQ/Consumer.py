import pika

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the same queue
channel.queue_declare(queue='vehicle_tasks')

# Callback function to process messages
def callback(ch, method, properties, body):
    print(f"Received: {body.decode()}")

# Consume messages from the queue
channel.basic_consume(queue='vehicle_tasks', on_message_callback=callback, auto_ack=True)

print("Waiting for messages. To exit press CTRL+C")
channel.start_consuming()

# Start consuming messages
channel.start_consuming()

