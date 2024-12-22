import pandas as pd
import numpy as np

# Generate sample data
np.random.seed(42)

def generate_sample_data(n_samples=1000):
    data = {
        'soil_temperature': np.random.uniform(10, 35, n_samples),  # Celsius
        'soil_moisture': np.random.uniform(20, 80, n_samples),     # Percentage
        'locationX': np.random.uniform(0, 100, n_samples),         # Field coordinates
        'locationY': np.random.uniform(0, 100, n_samples),         # Field coordinates
        'soil_ph': np.random.uniform(5.5, 7.5, n_samples),        # pH scale
        'air_temperature': np.random.uniform(15, 40, n_samples),   # Celsius
        'air_humidity': np.random.uniform(30, 90, n_samples)       # Percentage
    }
    
    # Define conditions for workability labels
    conditions = []
    for i in range(n_samples):
        # Unsafe conditions:
        if (data['soil_moisture'][i] > 70 or                  # Too wet
            data['soil_moisture'][i] < 30 or                  # Too dry
            data['soil_ph'][i] < 5.8 or                      # Too acidic
            data['soil_ph'][i] > 7.2):                       # Too alkaline
            conditions.append(2)  # Unsafe
        
        # Caution conditions:
        elif (60 < data['soil_moisture'][i] <= 70 or         # Slightly wet
              30 <= data['soil_moisture'][i] < 40 or         # Slightly dry
              5.8 <= data['soil_ph'][i] < 6.2 or            # Slightly acidic
              6.8 < data['soil_ph'][i] <= 7.2):             # Slightly alkaline
            conditions.append(1)  # Caution
        
        # Safe conditions:
        else:
            conditions.append(0)  # Safe
    
    data['condition'] = conditions
    
    return pd.DataFrame(data)

# Generate and save sample data
df = generate_sample_data(1000)
df.to_csv('agricultural_data.csv', index=False)
print("Sample of the generated data:")
print(df.head())
print("\nValue counts for conditions:")
print(df['condition'].value_counts())