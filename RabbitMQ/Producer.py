import pika

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a queue
channel.queue_declare(queue='vehicle_tasks')

# Send a message
message = "Navigate to Field A"
channel.basic_publish(exchange='', routing_key='vehicle_tasks', body=message)
print(f"Sent: {message}")

# Close connection
connection.close()


