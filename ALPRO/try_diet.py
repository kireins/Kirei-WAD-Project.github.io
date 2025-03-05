import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

# Load the dataset
df = pd.read_csv("diet_dataset.csv")


# Display basic information and first few rows
df.info(), df.head()


# Set style
sns.set(style="whitegrid")

# Create a figure for subplots
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Age distribution - Bar Chart
sns.countplot(x=df["Age"], palette="viridis", ax=axes[0])
axes[0].set_title("Age Distribution of Participants (Bar Chart)")
axes[0].set_xlabel("Age")
axes[0].set_ylabel("Count")
axes[0].tick_params(axis='x', rotation=45)

# Age distribution - Histogram
sns.histplot(df["Age"], bins=10, kde=True, color="blue", ax=axes[1])
axes[1].set_title("Age Distribution of Participants (Histogram)")
axes[1].set_xlabel("Age")
axes[1].set_ylabel("Frequency")

# Show plots
plt.tight_layout()
plt.show()

# Sleep Quality Distribution - Pie Chart
sleep_quality_counts = df["Sleep Quality"].value_counts()

# Plot pie chart
plt.figure(figsize=(7, 7))
plt.pie(sleep_quality_counts, labels=sleep_quality_counts.index, autopct='%1.1f%%', 
        colors=sns.color_palette("pastel"), startangle=140, wedgeprops={'edgecolor': 'black'})

plt.title("Distribution of Participants' Sleep Quality")
plt.show()

# Scatter plot: BMR vs. Daily Caloric Surplus/Deficit
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x="BMR (Calories)", y="Daily Caloric Surplus/Deficit", hue="Gender", palette="coolwarm")

plt.title("Relationship Between BMR and Daily Caloric Surplus/Deficit")
plt.xlabel("BMR (Calories)")
plt.ylabel("Daily Caloric Surplus/Deficit")
plt.legend(title="Gender")
plt.show()

# Box plot: Weight Loss vs. Physical Activity Level
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x="Physical Activity Level", y="Weight Change (lbs)", palette="Set2")

plt.title("Weight Change Based on Physical Activity Level")
plt.xlabel("Physical Activity Level")
plt.ylabel("Weight Change (lbs)")
plt.xticks(rotation=30)
plt.show()

# Detecting outliers using the IQR method
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1

# Define outlier boundaries
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter out outliers
df_cleaned = df[~((df < lower_bound) | (df > upper_bound)).any(axis=1)]

# Print data reduction summary
original_count = df.shape[0]
cleaned_count = df_cleaned.shape[0]
removed_outliers = original_count - cleaned_count

original_count, cleaned_count, removed_outliers


# Encoding categorical variables
categorical_cols = ["Gender", "Physical Activity Level", "Sleep Quality"]

# Apply Label Encoding
label_encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    df_cleaned[col] = le.fit_transform(df_cleaned[col])
    label_encoders[col] = le

# Display transformed data (first few rows)
df_cleaned.head()
