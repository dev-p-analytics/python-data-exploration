import pandas as pd
import matplotlib.pyplot as plt

# Initiliasing path to the data and loading it into a pandas dataframe
origin_path = "C:\\Dev\\Python\\intro_to_da\\Assignment 2\\25838323.csv"
df = pd.read_csv(origin_path)

#Overview of the data
print("Shape: ", df.shape)
print("\nData Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())
print("\nDescriptive Statistics:\n", df.describe())

#Grouping each column by attribute type
nominal_cols = ['gender', 'employment_status', 'loan_purpose', 'region', 'marital_status', 'loan_default']
ordinal_cols = ['education_level']
interval_cols = ['credit_score', 'application_year', 'application_date']
ratio_cols = ['age', 'income', 'loan_amount', 'debt_to_income_pct', 'num_dependents', 'years_employed', 'account_balance', 'num_prev_loans', 'monthly_expenses', 'loan_duration_months']