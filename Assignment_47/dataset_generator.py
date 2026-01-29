import numpy as np
import pandas as pd

# Set the seed for reproducibility
np.random.seed(42)

# Number of data points
n_samples = 14000

# Generate data for each feature
age = np.random.normal(60, 15, n_samples)
age = np.clip(age, 20, 100)  # Ensure age is within realistic bounds
bmi = np.random.normal(27, 5, n_samples)
bmi = np.clip(bmi, 15, 50)  # Ensure BMI within reasonable bounds
asa_status = np.random.choice([1, 2, 3, 4, 5], n_samples, p=[0.15, 0.25, 0.30, 0.20, 0.10])
baseline_cancer = np.random.choice([0, 1, 2, 3], n_samples, p=[0.4, 0.3, 0.2, 0.1])
baseline_charlson = np.random.normal(3, 2.5, n_samples)
baseline_charlson = np.clip(baseline_charlson, 0, 10)
hour = np.random.uniform(0, 24, n_samples)
hour = hour.astype(int)
month = np.random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], n_samples)
moonphase = np.random.uniform(0, 12, n_samples)
mort30 = np.random.normal(5, 5, n_samples)
mort30 = np.clip(mort30, 0, 30)
mortality_rsi = np.random.normal(3, 3, n_samples)
mortality_rsi = np.clip(mortality_rsi, 0, 10)
race = np.random.choice(['White', 'Black', 'Asian', 'Other'], n_samples, p=[0.6, 0.2, 0.1, 0.1])


# Corrected calculate_complication function
def calculate_complication(row):
    age = row[0]
    bmi = row[1]
    asa_status = row[2]
    baseline_cancer = row[3]
    baseline_charlson = row[4]
    hour = row[5]
    month = row[6]
    moonphase = row[7]
    mort30 = row[8]
    mortality_rsi = row[9]

    # Example equation - adjust coefficients as needed.
    probability = 0.5 + 0.001 * age - 0.005 * bmi + 0.1 * asa_status + 0.05 * baseline_cancer + 0.02 * baseline_charlson - 0.01 * hour + 0.005 * month + 0.01 * moonphase - 0.01 * mort30 - 0.02 * mortality_rsi
    probability = np.clip(probability, 0, 1)  # Ensure probability is between 0 and 1
    return probability


# Stack the arrays
stacked_arrays = np.stack(
    [age, bmi, asa_status, baseline_cancer, baseline_charlson, hour, month, moonphase, mort30, mortality_rsi], axis=1)

# Apply the function along axis 1 (rows)
complication_probabilities = np.apply_along_axis(calculate_complication, axis=1, arr=stacked_arrays)
complication = np.random.binomial(1, complication_probabilities)

# Create the DataFrame
data = pd.DataFrame({
    'Age': age,
    'BMI': bmi,
    'ASA_Status': asa_status,
    'Baseline_Cancer': baseline_cancer,
    'Baseline_Charlson': baseline_charlson,
    'Hour': hour,
    'Month': month,
    'Moonphase': moonphase,
    'mort30': mort30,
    'mortality_rsi': mortality_rsi,
    'Race': race,
    'Complication': complication
})

# Display the first few rows
print(data.head())

# Save the dataset to a CSV file
data.to_csv('synthetic_surgical_dataset.csv', index=False)
