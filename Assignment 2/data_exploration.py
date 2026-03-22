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

