 Task 1: Data Cleaning and Preprocessing – Data Analyst Internship

Objective
Clean and preprocess a raw marketing dataset by:
- Handling missing values
- Removing duplicate rows
- Standardizing text and date formats
- Renaming columns
- Correcting data types

This process prepares the dataset for analysis and ensures data quality.


Dataset Used

Name:Customer Personality Analysis

Filename: marketing_campaign.csv

Source:[Kaggle Dataset](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis)

Description:The dataset contains customer demographics, spending habits, and campaign response data. Useful for customer segmentation and marketing analysis.

Data Cleaning Steps Performed

1. Removed Duplicates
   - Used `drop_duplicates()` to eliminate any duplicate entries.

2. Handled Missing Values
   - Filled missing values in the `Income` column with the median.
   - Dropped remaining rows with missing values using `dropna()`.

3. Standardized Text Fields
   - Converted `Education` and `Marital_Status` to lowercase and removed extra spaces using `.str.lower().str.strip()`.

4. Converted Date Formats
   - Converted `Dt_Customer` column to consistent `datetime` format (`DD-MM-YYYY`).

5. Renamed Columns
   - Renamed all columns to `snake_case` using string methods to ensure consistency and readability.

6. Corrected Data Types
   - Created new `age` column from `Year_Birth` (2025 - Year_Birth).
   - Ensured `age` is an integer and `Dt_Customer` is in datetime format.


Tools Used
- Python 3.x
- Pandas
- VS code

Output Files
- `cleaned_marketing_campaign.csv` – Final cleaned dataset
- 'marketing_campaign' - actual dataset
- `data_cleaning.py` – Python script used for cleaning
- `README.md` – Documentation file (this file)


Kaggle Datasets Suitable for Task 1
- ✅ Customer Personality Analysis *(used)*



