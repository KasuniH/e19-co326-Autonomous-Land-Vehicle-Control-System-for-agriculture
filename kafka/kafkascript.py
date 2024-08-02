from kafka import KafkaProducer
import json
import logging
import time

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the Kafka broker
KAFKA_BROKER = 'pkc-12576z.us-west2.gcp.confluent.cloud:9092'
KAFKA_TOPIC = 'ditto-topic'

# Create a Kafka producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Define the data format
def create_vehicle_data(vehicle_id):
    return {
        "id": vehicle_id,
        "features": {
            "soil-temperature": {
                "properties": {
                    "value": 123
                }
            },
            "soil-moisture": {
                "properties": {
                    "value": 24
                }
            },
            "locationX": {
                "properties": {
                    "value": 123
                }
            },
            "locationY": {
                "properties": {
                    "value": 123
                }
            },
            "soil-ph": {
                "properties": {
                    "value": 3123
                }
            },
            "air-temperature": {
                "properties": {
                    "value": 123
                }
            },
            "air-humidity": {
                "properties": {
                    "value": 4223
                }
            }
        }
    }

try:
    while True:
        for vehicle_id in range(1, 4):  # Assuming we have 3 vehicles
            data = create_vehicle_data(f'vehicle-{vehicle_id}')
            
            # Ensure data is JSON format
            if not isinstance(data, str):
                data = json.dumps(data)
                
            producer.send(KAFKA_TOPIC, value=data)
            logger.info(f"Sent data to Kafka: {data}")
            
        time.sleep(10)  # Adjust the interval as needed

except KeyboardInterrupt:
    producer.close()
    logger.info("Kafka producer closed.")