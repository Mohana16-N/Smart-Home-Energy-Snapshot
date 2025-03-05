import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Sample dataset (energy usage based on time & power)
data = {
    "time_of_day": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
    "power_consumed": [50, 48, 47, 46, 50, 60, 90, 120, 150, 160, 170, 180, 200, 210, 220, 230, 220, 210, 190, 180, 150, 120, 80, 60]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Split dataset
X = df[["time_of_day"]]
y = df["power_consumed"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

def predict_energy(time_of_day: int):
    """Predict energy consumption based on time of day."""
    prediction = model.predict([[time_of_day]])
    return max(0, prediction[0])  # Ensure non-negative values
