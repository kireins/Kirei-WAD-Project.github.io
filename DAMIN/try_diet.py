import pandas as pd

# Load the dataset (ensure the correct file path)
file_path = "diet_dataset.csv"  # Update if needed
df = pd.read_csv(file_path)

# Display column names to check for inconsistencies
print("Column Names:", df.columns)

# Creating a copy to avoid modifying the original dataset
data_encoded = df.copy()

# Encoding 'Gender' (handling missing values)
data_encoded['Gender'] = data_encoded['Gender'].fillna('Unknown').replace({'M': 0, 'F': 1})

# Encoding 'Physical Activity Level' (ensure column name matches dataset)
activity_mapping = {'Sedentary': 0, 'Lightly Active': 1, 'Moderately Active': 2, 'Very Active': 3}
data_encoded['Physical Activity Level'] = data_encoded['Physical Activity Level'].replace(activity_mapping)

# Encoding 'Sleep Quality' (ensure column name matches dataset)
sleep_mapping = {'Poor': 0, 'Fair': 1, 'Good': 2, 'Excellent': 3}
data_encoded['Sleep Quality'] = data_encoded['Sleep Quality'].replace(sleep_mapping)

# Display encoded dataset
print("\nEncoded Dataset:")
print(data_encoded.head())  # Show first few rows for clarity

# Ensure the output matches the desired format
print("\nTransformed Dataset:")
print(data_encoded.to_string(index=False))
