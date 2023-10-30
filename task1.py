import pandas as pd

# Read the dataset from the provided path
file_path = r'C:\Users\91756\Downloads\train.csv'
df = pd.read_csv(file_path)

# Removing missing values in the 'Age', 'Fare', 'Cabin', and 'Embarked' columns
df_cleaned = df.dropna(subset=['Age', 'Fare', 'Cabin', 'Embarked'])

# Removing outliers in the 'Age' column using IQR method
Q1_age = df_cleaned['Age'].quantile(0.25)
Q3_age = df_cleaned['Age'].quantile(0.75)
IQR_age = Q3_age - Q1_age
lower_bound_age = Q1_age - 1.5 * IQR_age
upper_bound_age = Q3_age + 1.5 * IQR_age

outliers_age = (df_cleaned['Age'] < lower_bound_age) | (df_cleaned['Age'] > upper_bound_age)
df_cleaned = df_cleaned[~outliers_age]

# Removing outliers in the 'Fare' column using IQR method
Q1_fare = df_cleaned['Fare'].quantile(0.25)
Q3_fare = df_cleaned['Fare'].quantile(0.75)
IQR_fare = Q3_fare - Q1_fare
lower_bound_fare = Q1_fare - 1.5 * IQR_fare
upper_bound_fare = Q3_fare + 1.5 * IQR_fare

outliers_fare = (df_cleaned['Fare'] < lower_bound_fare) | (df_cleaned['Fare'] > upper_bound_fare)
df_cleaned = df_cleaned[~outliers_fare]

# Reset the index to avoid gaps after removing rows and sort by 'PassengerId'
df_cleaned.sort_values(by='PassengerId', inplace=True)
df_cleaned.reset_index(drop=True, inplace=True)

# Assign new 'PassengerId' values from 1 to 168
df_cleaned['PassengerId'] = range(1, len(df_cleaned) + 1)

# Save the cleaned data to a new CSV file
cleaned_file_path = r'C:\Users\91756\Downloads\cleaned_train.csv'
df_cleaned.to_csv(cleaned_file_path, index=False)

print(f"Cleaned data has been saved to: {cleaned_file_path}")
