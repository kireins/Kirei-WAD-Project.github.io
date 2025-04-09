import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score



df = pd.read_csv("diet_dataset.csv")

# print(df.head())
# print(df.info())
# print(df.describe())

# # Select True Value Column
# values = df['Age']  

# # Scope setting and classification
# bins = [10, 20, 30, 40, 50, 60] #define scope
# labels = ["10-19", "20-29", "30-39", "40-49", "50-59"]  #label of scope
# df['Age'] = pd.cut(values, bins=bins, labels=labels, right=False)

# # Calculate the number of data by range
# range_counts = df['Age'].value_counts(sort=False)

# # Plot bar chart
# plt.figure(figsize=(8, 5))  
# plt.bar(range_counts.index.astype(str), range_counts.values, width=0.5, color='lightsteelblue') 
# plt.xlabel("Age")  
# plt.ylabel("frequent")       
# plt.title("Age distribution")  
# plt.xticks(rotation=45)  
# plt.tight_layout()  
# plt.show()


# #Plot by histogram
# df['Age'].plot.hist(bins=20, color='lightcoral', alpha=0.7, edgecolor='darkblue')
# plt.title('Age Distribution')
# plt.xlabel('Age')
# plt.ylabel('Frequency')
# plt.show()


# Calculate the number of characters per value
# value_counts = df['Sleep Quality'].value_counts()

# # Plot pie chart
# plt.figure(figsize=(7, 7)) 
# plt.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightgreen', 'orange', 'pink'])
# plt.title("Sleep Quality") 
# plt.show()

# df_subset = df[['Age', 'Current Weight (lbs)', 'BMR (Calories)','Daily Calories Consumed']]

# scatter_matrix(df_subset, alpha=0.5, figsize=(10, 6), diagonal='hist')
# plt.show()

# df['loss weight(lbs)'] = df['Current Weight (lbs)'] - df['Final Weight (lbs)']

# grouped_data = df.groupby('Physical Activity Level')['loss weight(lbs)']

# for name, group in grouped_data:
#     print(name)  
#     for value in group:
#         print(f"{value:.2f}")  
#     print()

# 'loss weight(lbs)'
df['loss weight(lbs)'] = df['Current Weight (lbs)'] - df['Final Weight (lbs)']

plt.figure(figsize=(8, 6))

activity_order = ['Sedentary', 'Lightly Active', 'Moderately Active', 'Very Active']

# Plot boxplot
sns.boxplot(x='Physical Activity Level', y='loss weight(lbs)', data=df, order=activity_order, 
            boxprops=dict(color='slategrey'), 
            whiskerprops=dict(color='black'), 
            capprops=dict(color='black'),     
            flierprops=dict(markerfacecolor='green', marker='o', markersize=5), 
            medianprops=dict(color='yellow')) 

# Add titles and labels
plt.title('Boxplot of Weight Loss by Physical Activity Level')
plt.xlabel('Physical Activity Level')
plt.ylabel('Weight Loss (lbs)')

# plt.show()

Q1 = df['loss weight(lbs)'].quantile(0.25)
Q3 = df['loss weight(lbs)'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 2 * IQR
upper_bound = Q3 + 2 * IQR

data_cleaned = df[(df['loss weight(lbs)'] >= lower_bound) & (df['loss weight(lbs)'] <= upper_bound)]

# after outlier treatment
plt.figure(figsize=(8, 6))

sns.boxplot(x='Physical Activity Level', y='loss weight(lbs)', data=data_cleaned, order=activity_order, 
            boxprops=dict(color='slategrey'), 
            whiskerprops=dict(color='black'), 
            capprops=dict(color='black'),     
            flierprops=dict(markerfacecolor='green', marker='o', markersize=5), 
            medianprops=dict(color='yellow')) 

plt.title('Boxplot of Weight Loss by Physical Activity Level (After Outlier Removal)')
plt.xlabel('Physical Activity Level')
plt.ylabel('Weight Loss (lbs)')

# plt.show()

pd.set_option('future.no_silent_downcasting', True)

data_encoded = df.copy()

# 'Gender' encoding
data_encoded['Gender'] = data_encoded['Gender'].fillna('Unknown').replace({'M': 0, 'F': 1,})

# 'Physical Activity Level' endocing
activity_mapping = {'Sedentary': 0, 'Lightly Active': 1, 'Moderately Active': 2, 'Very Active': 3}
data_encoded['Physical Activity Level'] = data_encoded['Physical Activity Level'].replace(activity_mapping)

# 'Sleep Quality' encoding
sleep_mapping = {'Poor': 0, 'Fair': 1, 'Good': 2, 'Excellent': 3}
data_encoded['Sleep Quality'] = data_encoded['Sleep Quality'].replace(sleep_mapping)

# print(data_encoded)









#DATA MODELING
# N
# 1. Buat kategori baru dari data yang sudah di ubah, lalu di beri label value. 
def categorize_weight_change(value):
    """Categorize weight change based on the given value."""
    if value < -2: #kurang dari -2 berarti turun berat badan
        return 'Weight Loss'
    elif -2 <= value <= 2: # antara -2 dan 2 berarti tidak ada perubahan berat badan
        return 'No Change'
    else:
        return 'Weight Gain' # lebih dari 2 berarti naik berat badan

# N
# 2. Buat kolom baru 'Weight Change Category' berdasarkan kolom 'Weight Change (lbs)'
data_encoded['Weight Change Category'] = data_encoded['Weight Change (lbs)'].map(
    lambda x: categorize_weight_change(x)
)
# N
# 3. Ubah target kategori  menjadi angka menggunakan LabelEncoder
label_encoder = LabelEncoder()
data_encoded['Weight Change Category Encoded'] = label_encoder.fit_transform(
    data_encoded['Weight Change Category']
)
# K
# 4. Mempersiapkan data untuk training dan testing
X = data_encoded[['Weight Change (lbs)']]  
y = data_encoded['Weight Change Category Encoded']

# K
# 5. Memisahkan data menjadi training dan testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# K
# 6. Menggunakan Logistic Regression untuk memprediksi kategori perubahan berat badan
logreg = LogisticRegression()
logreg.fit(X_train, y_train)

# K
# 7. Memprediksi kategori perubahan berat badan pada data testing
y_pred = logreg.predict(X_test)

# K
# 8. Menghitung akurasi
print("Accuracy:", accuracy_score(y_test, y_pred))

# N
# 9. Menghitung classification report
print("Classification Report:\n", classification_report(y_test, y_pred))