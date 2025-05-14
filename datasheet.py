# Import required libraries
import pandas as pd

# Load the dataset
df = pd.read_csv('marketing_campaign.csv', sep='\t') 

# Initial overview
print("Initial Dataset Shape:", df.shape)
print("\nMissing Values:\n", df.isnull().sum())

# 1. Remove duplicate rows
df = df.drop_duplicates()
print("\nRemoved duplicates. New shape:", df.shape)

# 2. Handle missing values
# Checking columns with missing values
missing_cols = df.columns[df.isnull().any()]
print("\nColumns with missing values:", missing_cols.tolist())

# Example: Fill missing 'Income' with median
if 'Income' in df.columns:
    df['Income'] = df['Income'].fillna(df['Income'].median())
    print("Filled missing values in 'Income' with median.")

# Drop remaining rows with missing values 
df = df.dropna()
print("Dropped remaining rows with missing values. New shape:", df.shape)

# 3. Standardize categorical/text data
text_columns = ['Education', 'Marital_Status']
for col in text_columns:
    if col in df.columns:
        df[col] = df[col].astype(str).str.lower().str.strip()

# 4. Convert date columns to consistent format
if 'Dt_Customer' in df.columns:
    df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], format='%d-%m-%Y')
    print("Converted 'Dt_Customer' to datetime format.")

# 5. Rename columns (snake_case, no spaces)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
print("Renamed columns to snake_case format.")

# 6. Fix numeric columns (e.g., age)
if 'year_birth' in df.columns:
    df['age'] = 2025 - df['year_birth']  # Assuming current year = 2025
    print("Created new 'age' column from 'year_birth'.")

# 7. Final checks
print("\nFinal Dataset Info:")
print(df.info())

# 8. Save cleaned dataset
df.to_csv('cleaned_marketing_campaign.csv', index=False)
print("\nCleaned dataset saved as 'cleaned_marketing_campaign.csv'.")
