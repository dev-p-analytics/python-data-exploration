from data import df, ratio_cols, nominal_cols, ordinal_cols, interval_cols, missing_cols
import pandas as pd

def summarise_ratio(col):
    print("-" * 40)
    print(f"\nSummary for: {col}")
    print("-" * 40)

    data = df[col]
    data_clean = data.dropna()  # Remove missing values for summary statistics

    # Stats excluding missing values (pandas default behavior)
    print(f"Mean (excluding missing values): {data.mean():.2f}")
    print(f"Median (excluding missing values): {data.median():.2f}")
    print(f"Mode (excluding missing values): {data.mode().iloc[0]:.2f}")
    print(f"Standard Deviation (excluding missing values): {data.std():.2f}")
    print(f"Variance (excluding missing values): {data.var():.2f}")
    print(f"Min (excluding missing values): {data.min():.2f}")
    print(f"Max (excluding missing values): {data.max():.2f}")
    print(f"25th Percentile (excluding missing values): {data.quantile(0.25):.2f}")
    print(f"50th Percentile (excluding missing values): {data.quantile(0.50):.2f}")
    print(f"75th Percentile (excluding missing values): {data.quantile(0.75):.2f}")
    print(f"Skewness (excluding missing values): {data.skew():.2f}") 
    print(f"Missing Values: {data.isnull().sum()}")

    if data.isnull().sum() > 0:
        print(f"                   Excluding Missing  -->  Including Missing")
        print(f"Mean:              {data_clean.mean():.2f}    -->  {data.mean():.2f}")
        print(f"Median:            {data_clean.median():.2f}    -->  {data.median():.2f}")
        print(f"Mode:              {data_clean.mode().iloc[0]:.2f}    -->  {data.mode().iloc[0]:.2f}")
        print(f"Standard Deviation: {data_clean.std():.2f}    -->  {data.std():.2f}")
        print(f"Variance:          {data_clean.var():.2f}    -->  {data.var():.2f}")
        print(f"Min:               {data_clean.min():.2f}    -->  {data.min():.2f}")
        print(f"Max:               {data_clean.max():.2f}    -->  {data.max():.2f}")
        print(f"25th Percentile:   {data_clean.quantile(0.25):.2f}    -->  {data.quantile(0.25):.2f}")
        print(f"50th Percentile:   {data_clean.quantile(0.50):.2f}    -->  {data.quantile(0.50):.2f}")
        print(f"75th Percentile:   {data_clean.quantile(0.75):.2f}    -->  {data.quantile(0.75):.2f}")
        print(f"Skewness:          {data_clean.skew():.2f}    -->  {data.skew():.2f}")
        print(f"N (observations):  {len(data_clean)}    -->  {len(data)}")  # Shows difference in sample size

def summarise_nominal(col):
    print("-" * 40)
    print(f"\nSummary for: {col}")
    print("-" * 40)

    data = df[col]
    data_clean = data.dropna()  # Remove missing values for summary statistics

    # Frequency and relative frequency (including NaN for "including missing")
    freq = data.value_counts(dropna=False)  # Include NaN as a category
    rel_freq = data.value_counts(normalize=True, dropna=False) * 100

    print(f"Mode (excluding missing values): {data.mode().iloc[0]}")  # Mode excludes NaN
    print(f"Missing Values: {data.isnull().sum()}")

    if col in missing_cols:
        print(f"\n                   Excluding Missing  -->  Including Missing")
        print(f"\nMode:              {data_clean.mode().iloc[0]}    -->  {data.mode().iloc[0]}")
        # Loop through all categories, including NaN
        for category in freq.index:
            if pd.isna(category):  # Handle NaN category
                clean_count = 0
                clean_rel = 0.0
                cat_label = "NaN"
            else:
                clean_count = data_clean.value_counts().get(category, 0)
                clean_rel = data_clean.value_counts(normalize=True).get(category, 0) * 100
                cat_label = str(category)
            print(f"{cat_label}: {clean_count} ({clean_rel:.2f}%)    -->  {freq[category]} ({rel_freq[category]:.2f}%)")
    else:
        for category in freq.index:
            cat_label = "NaN" if pd.isna(category) else str(category)
            print(f"{cat_label}: {freq[category]} ({rel_freq[category]:.2f}%)")

if __name__ == "__main__":
    for col in ratio_cols:
        summarise_ratio(col)
    for col in nominal_cols:
        summarise_nominal(col)