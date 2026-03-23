import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Initiliasing path to the data and loading it into a pandas dataframe
origin_path = "C:\\Dev\\Python\\intro_to_da\\Assignment 2\\25838323.csv"
df = pd.read_csv(origin_path)

#Overview of the data
print("Shape: ", df.shape)                          # Number of rows and columns
print("\nData Types:\n", df.dtypes)                 # What data types are in each column    
print("\nMissing Values:\n", df.isnull().sum())     # Number of missing values in each column
print("\nDescriptive Statistics:\n", df.describe()) # Summary statistics for numerical columns

#Grouping each column by attribute type
nominal_cols = ['gender', 'employment_status', 'loan_purpose', 'region', 'marital_status', 'loan_default']
ordinal_cols = ['education_level']
interval_cols = ['credit_score', 'application_year', 'application_date']
ratio_cols = ['age', 'income', 'loan_amount', 'debt_to_income_pct', 'num_dependents', 'years_employed', 'account_balance', 'num_prev_loans', 'monthly_expenses', 'loan_duration_months']

#Missing Columns
missing_cols = df.columns[df.isnull().any()].tolist()
print("\nColumns with Missing Values:\n", missing_cols)

def summarise_ratio(col):
    print("-" * 40)
    print(f"\nSummary for: {col}")
    print("-" * 40)

    data = df[col]
    data_clean = data.dropna()  # Remove missing values for summary statistics

    # Stats with missing values included
    print(f"Mean (with missing values): {data.mean():.2f}")
    print(f"Median (with missing values): {data.median():.2f}")
    print(f"Mode (with missing values): {data.mode().iloc[0]:.2f}")
    print(f"Standard Deviation (with missing values): {data.std():.2f}")
    print(f"Variance (with missing values): {data.var():.2f}")
    print(f"Min (with missing values): {data.min():.2f}")
    print(f"Max (with missing values): {data.max():.2f}")
    print(f"25th Percentile (with missing values): {data.quantile(0.25):.2f}")
    print(f"50th Percentile (with missing values): {data.quantile(0.50):.2f}")
    print(f"75th Percentile (with missing values): {data.quantile(0.75):.2f}")
    print(f"Skewness (with missing values): {data.skew():.2f}") 
    print(f"Missing Values: {data.isnull().sum()}")

    if col in missing_cols:
        print(f"                   Without Missing  -->  With Missing")
        print(f"Mean:              {data_clean.mean():.2f}    -->  {data.mean():.2f}")
        print(f"Median:            {data_clean.median():.2f}    -->  {data.median():.2f}")
        print(f"Mode:              {data_clean.mode().iloc[0]:.2f}    -->  {data.mode().iloc[0]:.2f}")
        print(f"Standard Deviation: {data_clean.std():.2f}    -->  {data.std():.2f}")
        print(f"Variance:          {data_clean.var():.2f}    -->  {data.var():.2f}")
        print(f"Min:               {data_clean.min():.2f}    -->  {data.min():.2f}")
        print(f"Max:               {data_clean.max():.2f}    -->  {data.max():.2f}")
        print(f"25th Percentile:   {data_clean.quantile(0.25    ):.2f}    -->  {data.quantile(0.25):.2f}")
        print(f"50th Percentile:   {data_clean.quantile(0.50    ):.2f}    -->  {data.quantile(0.50):.2f}")
        print(f"75th Percentile:   {data_clean.quantile(0.75    ):.2f}    -->  {data.quantile(0.75):.2f}")
        print(f"Skewness:          {data_clean.skew():.2f}    -->  {data.skew():.2f}")

for col in ratio_cols:
    summarise_ratio(col)