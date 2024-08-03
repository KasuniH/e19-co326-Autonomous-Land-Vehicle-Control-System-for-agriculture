import time
import json
import random
from kafka import KafkaProducer


class Vehicle:
    def __init__(self, vehicle_id):
        self.vehicle_id = vehicle_id
        self.soil_temperature = self.random_soil_temp_cels()
        self.soil_moisture = self.random_soil_moisture()
        self.locationX = self.random_location()
        self.locationY = self.random_location()
        self.soil_ph = self.random_soil_ph()
        self.air_temperature = self.random_air_temp_cels()
        self.air_humidity = self.random_air_humidity()

    def random_soil_temp_cels(self):
        return round(random.uniform(10, 30), 1)

    def random_soil_moisture(self):
        return round(random.uniform(0, 100), 1)

    def random_location(self):
        return round(random.uniform(0, 100), 1)

    def random_soil_ph(self):
        return round(random.uniform(5.0, 9.0), 1)

    def random_air_temp_cels(self):
        return round(random.uniform(15, 35), 1)

    def random_air_humidity(self):
        return round(random.uniform(20, 100), 1)


def get_json_data(vehicle):
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
    return json.dumps(data)


def main():
    producer = KafkaProducer(bootstrap_servers=['34.42.82.181:9092'])

    vehicle_ids = ["Vehicle-1", "Vehicle-2", "Vehicle-3"]
    vehicles = [Vehicle(vehicle_id) for vehicle_id in vehicle_ids]

    for _ in range(20000):
        for vehicle in vehicles:
            json_data = get_json_data(vehicle)
            producer.send('opentwins', value=bytes(json_data, 'utf-8'))
            print(f"Sensor data sent for {vehicle.vehicle_id}: {json_data}")
        time.sleep(5)

if __name__ == "__main__":
    main()
