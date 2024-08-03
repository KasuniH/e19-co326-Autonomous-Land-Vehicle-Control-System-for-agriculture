import json
from kafka import KafkaConsumer, KafkaProducer

class Vehicle:
    def __init__(self):
        self.soil_temperature = 0
        self.soil_moisture = 0
        self.locationX = 0
        self.locationY = 0
        self.soil_ph = 0
        self.air_temperature = 0
        self.air_humidity = 0
        self.vehicle_id = ""

def create_data(vehicle):
    data = {
        "soil-temperature": vehicle.soil_temperature,
        "soil-moisture": vehicle.soil_moisture,
        "locationX": vehicle.locationX,
        "locationY": vehicle.locationY,
        "soil-ph": vehicle.soil_ph,
        "air-temperature": vehicle.air_temperature,
        "air-humidity": vehicle.air_humidity,
        "vehicle_id": vehicle.vehicle_id
    }
    return data

vehicle_arr = []

for i in range(1, 4):
    vehicle = Vehicle()
    vehicle.vehicle_id = f"vehicle-{i}"
    vehicle_arr.append(vehicle)

# Kafka configuration
bootstrap_servers = '34.42.82.181:9092'
consumer_topic = 'opentwins'
producer_topic = 'opentwins'

# Create Kafka consumer and producer
consumer = KafkaConsumer(
    consumer_topic,
    bootstrap_servers=bootstrap_servers,
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers,
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

def process_message(message_json):

    if 'path' not in message_json or 'value' not in message_json:
        # print("Invalid message format")
        return

    vehicle_id = message_json['topic'].split('/')[1]
    feature = message_json['path'].split('/')[2]
    value = message_json['value']

    vehicle = None
    for i in vehicle_arr:
        if i.vehicle_id == vehicle_id:
            vehicle = i
            break

    if vehicle is None:
        print(f"Vehicle with ID {vehicle_id} not found")
        return

    if feature == "soil-temperature":
        vehicle.soil_temperature = value
    elif feature == "soil-moisture":
        vehicle.soil_moisture = value
    elif feature == "locationX":
        vehicle.locationX = value
    elif feature == "locationY":
        vehicle.locationY = value
    elif feature == "soil-ph":
        vehicle.soil_ph = value
    elif feature == "air-temperature":
        vehicle.air_temperature = value
    elif feature == "air-humidity":
        vehicle.air_humidity = value

    data = create_data(vehicle)
    return data

def consume_messages():
    try:
        for message in consumer:
            message_json = message.value
            processed_data = process_message(message_json)
            if processed_data:
                producer.send(producer_topic, value=processed_data)
                print(f"Processed data sent for vehicle {processed_data['vehicle_id']}: {processed_data}")
    except KeyboardInterrupt:
        print("Aborted by user")
    finally:
        consumer.close()
        producer.close()

if __name__ == "__main__":
    consume_messages()
