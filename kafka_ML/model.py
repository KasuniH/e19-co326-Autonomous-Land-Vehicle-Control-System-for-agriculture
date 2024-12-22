import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.utils import to_categorical


class SoilWorkabilityModel:
    def __init__(self):
        self.model = None
        self.scaler = StandardScaler()

    def load_and_preprocess_data(self, data_path):
        # Load data
        df = pd.read_csv(data_path)

        # Separate features and target
        X = df[
            [
                "soil_temperature",
                "soil_moisture",
                "locationX",
                "locationY",
                "soil_ph",
                "air_temperature",
                "air_humidity",
            ]
        ]
        y = df["condition"]

        # Scale features
        X_scaled = self.scaler.fit_transform(X)

        # Convert target to categorical
        y_cat = to_categorical(y, num_classes=3)

        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X_scaled, y_cat, test_size=0.2, random_state=42
        )

        return X_train, X_test, y_train, y_test

    def build_model(self):
        self.model = tf.keras.Sequential(
            [
                tf.keras.layers.Dense(64, activation="relu", input_shape=(7,)),
                tf.keras.layers.BatchNormalization(),
                tf.keras.layers.Dropout(0.2),
                tf.keras.layers.Dense(32, activation="relu"),
                tf.keras.layers.BatchNormalization(),
                tf.keras.layers.Dropout(0.2),
                tf.keras.layers.Dense(16, activation="relu"),
                tf.keras.layers.Dense(3, activation="softmax"),
            ]
        )

        self.model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
            loss="categorical_crossentropy",
            metrics=["accuracy"],
        )

        return self.model

    def train(self, X_train, y_train, X_test, y_test, epochs=50):
        # Early stopping callback
        early_stopping = tf.keras.callbacks.EarlyStopping(
            monitor="val_loss", patience=5, restore_best_weights=True
        )

        # Training
        history = self.model.fit(
            X_train,
            y_train,
            epochs=epochs,
            batch_size=32,
            validation_data=(X_test, y_test),
            callbacks=[early_stopping],
        )

        return history

    def predict_single_sample(self, sample_data):
        """
        Predict soil workability for a single sample
        sample_data should be a dictionary with all required features
        """
        # Convert sample to DataFrame
        sample_df = pd.DataFrame([sample_data])

        # Scale the sample
        scaled_sample = self.scaler.transform(sample_df)

        # Make prediction
        prediction = self.model.predict(scaled_sample)

        # Get the predicted class and probabilities
        predicted_class = np.argmax(prediction[0])
        probabilities = prediction[0]

        # Convert to human-readable result
        conditions = {0: "Safe", 1: "Caution", 2: "Unsafe"}
        result = {
            "condition": conditions[predicted_class],
            "safe_probability": float(probabilities[0]),
            "caution_probability": float(probabilities[1]),
            "unsafe_probability": float(probabilities[2]),
        }

        return result


def main():
    # Initialize model
    soil_model = SoilWorkabilityModel()

    # Load and preprocess data
    X_train, X_test, y_train, y_test = soil_model.load_and_preprocess_data(
        "agricultural_data.csv"
    )

    # Build model
    model = soil_model.build_model()
    print(model.summary())

    # Train model
    history = soil_model.train(X_train, y_train, X_test, y_test)

    # Test prediction with a sample
    sample_data = {
        "soil_temperature": 25.0,
        "soil_moisture": 45.0,
        "locationX": 50.0,
        "locationY": 50.0,
        "soil_ph": 6.5,
        "air_temperature": 28.0,
        "air_humidity": 60.0,
    }

    result = soil_model.predict_single_sample(sample_data)
    print("\nSample Prediction:")
    print(f"Predicted Condition: {result['condition']}")
    print(f"Safe Probability: {result['safe_probability']:.2f}")
    print(f"Caution Probability: {result['caution_probability']:.2f}")
    print(f"Unsafe Probability: {result['unsafe_probability']:.2f}")


if __name__ == "__main__":
    main()
