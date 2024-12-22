import sys
sys.path.append(sys.path[0] + "/../..") 
from datasources.raw_sink import RawSink
import pandas as pd
import numpy as np
import logging

logging.basicConfig(level=logging.INFO)

def load_agricultural_data(csv_path):
    """
    Load and preprocess agricultural sensor data from CSV
    Expected CSV columns: soil_temperature, soil_moisture, locationX, locationY, 
                         soil_ph, air_temperature, air_humidity, workability_label
    """
    # Read CSV file
    df = pd.read_csv(csv_path)
    
    # Separate features and labels
    features = df.drop('workability_label', axis=1).values
    labels = df['workability_label'].values
    
    # Split into train/test sets (80/20 split)
    train_size = int(0.8 * len(features))
    
    x_train = features[:train_size]
    y_train = labels[:train_size]
    x_test = features[train_size:]
    y_test = labels[train_size:]
    
    return (x_train, y_train), (x_test, y_test)

# Initialize Kafka-ML sink
# Using deployment_id=1 - make sure this matches your Kafka-ML deployment
agricultural_sink = RawSink(
    boostrap_servers='localhost:9094',
    topic='agricultural_data',
    deployment_id=1,
    description='Agricultural sensor data for soil workability prediction',
    validation_rate=0.1,
    test_rate=0.1
)

# Load and send data
try:
    
    csv_path = 'agricultural_data.csv'
    
    # Load the data
    (x_train, y_train), (x_test, y_test) = load_agricultural_data(csv_path)
    
    logging.info(f"Training data shape: {x_train.shape}")
    logging.info(f"Test data shape: {x_test.shape}")
    
    # Send training data
    for (x, y) in zip(x_train, y_train):
        agricultural_sink.send(data=x, label=y)
        
    # Send test data
    for (x, y) in zip(x_test, y_test):
        agricultural_sink.send(data=x, label=y)
        
    logging.info("Successfully sent all data to Kafka-ML")

except Exception as e:
    logging.error(f"Error occurred: {str(e)}")

finally:
    agricultural_sink.close()
