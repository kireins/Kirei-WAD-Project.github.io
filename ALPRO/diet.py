import pandas as pd
df = pd.read_csv("diet_dataset.csv")
duplicates = df.duplicated()
print(df)  
print(df.isnull().sum())  
print(df['Gender'].unique())  
Q1 = df['Stress Level'].quantile(0.25)
Q3 = df['Stress Level'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['Stress Level'] < (Q1 - 1.5 * IQR)) | (df['Stress Level'] > (Q3 + 1.5 * IQR))]
print(outliers)




