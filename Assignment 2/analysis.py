from data import df, ratio_cols, nominal_cols, ordinal_cols, interval_cols, missing_cols
import pandas as pd


def safe_mode(series):
    mode_vals = series.mode(dropna=True)
    return mode_vals.iloc[0] if len(mode_vals) > 0 else None


def summarise_ratio(col):
    print("-" * 40)
    print(f"\nSummary for: {col}")
    print("-" * 40)

    data = df[col]
    data_clean = data.dropna()  # Remove missing values for summary statistics

    # Stats excluding missing values (pandas default behavior)
    mode_val = safe_mode(data_clean)
    mode_str = f"{mode_val:.2f}" if pd.notna(mode_val) else "None"

    print(f"Mean (excluding missing values): {data.mean():.2f}")
    print(f"Median (excluding missing values): {data.median():.2f}")
    print(f"Mode (excluding missing values): {mode_str}")
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
        mode_clean = safe_mode(data_clean)
        mode_all = safe_mode(data)
        mode_clean_str = f"{mode_clean:.2f}" if pd.notna(mode_clean) else "None"
        mode_all_str = f"{mode_all:.2f}" if pd.notna(mode_all) else "None"

        print(f"Mean:              {data_clean.mean():.2f}    -->  {data.mean():.2f}")
        print(f"Median:            {data_clean.median():.2f}    -->  {data.median():.2f}")
        print(f"Mode:              {mode_clean_str}    -->  {mode_all_str}")
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

    mode_val = safe_mode(data_clean)
    mode_all = safe_mode(data)
    print(f"Mode (excluding missing values): {mode_val}")  # Mode excludes NaN
    print(f"Missing Values: {data.isnull().sum()}")

    if col in missing_cols:
        print(f"\n                   Excluding Missing  -->  Including Missing")
        print(f"\nMode:              {mode_val}    -->  {mode_all}")
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

def summarise_ordinal(col):
    print("-" * 40)
    print(f"\nSummary for: {col}")
    print("-" * 40)

    data = df[col]
    data_clean = data.dropna()

    # Quick special-case for large unique date lists
    if col == 'application_date':
        print(f"Min date: {data.min()}")
        print(f"Max date: {data.max()}")
        print(f"Unique dates (non-null): {data_clean.nunique()}")
        print("Top 10 frequent dates:")
        print(data.value_counts(dropna=False).head(10))
        return

    #Frequency and Relative Frequency
    freq = data.value_counts(dropna=False)  # Include NaN as a category
    rel_freq = data.value_counts(normalize=True, dropna=False) * 100

    # Cumulative Frequency
    freq_no_null = data.value_counts(dropna=True)
    cum_freq = freq_no_null.cumsum()

    mode_val = safe_mode(data)
    print(f"Mode: {mode_val}")  # Mode excludes NaN
    print(f"Missing Values: {data.isnull().sum()}")

    print (f"\nFrequency, Relative & Cumulative Frequency: ")
    for category in freq_no_null.index:
        print(f"  {str(category):<25} count: {freq_no_null[category]:<8} ({rel_freq[category]:.2f}%)   cumulative: {cum_freq[category]}")

    # Impact of missing values
    if col in missing_cols:
        print(f"\n   Impact of Missing Values")
        print(f"{'category':<25} {'Excl. Missing':>15} {'Incl. Missing':>15}")
        rel_freq_clean = data_clean.value_counts(normalize=True) * 100
        for category in freq.index:
            print(f" {str(category):<25} {rel_freq_clean.get(category, 0):>15.2f}% {rel_freq[category]:>15.2f}%")

def summarise_interval(col):
    print("-" * 40)
    print(f"\nSummary for: {col}")
    print("-" * 40)

    data = df[col]
    if not pd.api.types.is_numeric_dtype(data):
        print(f"{col} is not numeric (dtype={data.dtype}); skipping interval statistics.")
        return

    data_clean = data.dropna()  # Remove missing values for summary statistics
    
    # interval has no true zero; no skewness
    mode_val = safe_mode(data_clean)
    mode_str = f"{mode_val:.2f}" if pd.notna(mode_val) else "None"
    print(f"Mean: {data.mean():.2f}")
    print(f"Median: {data.median():.2f}")
    print(f"Mode: {mode_str}")
    print(f"Min: {data.min():.2f}")
    print(f"Max: {data.max():.2f}")
    print(f"Range: {data.max() - data.min():.2f}")
    print(f"Variance: {data.var():.2f}")
    print(f"Standard Deviation: {data.std():.2f}")
    print(f"25th Percentile: {data.quantile(0.25):.2f}")
    print(f"50th Percentile: {data.quantile(0.50):.2f}")
    print(f"75th Percentile: {data.quantile(0.75):.2f}")
    print(f"Missing Values: {data.isnull().sum()}")

    if col in missing_cols:
        print(f"\n   Impact of Missing Values")
        print(f"              Excluding Missing  -->  Including Missing")
        print(f"Mean:         {data_clean.mean():.2f}    -->  {data.mean():.2f}")
        print(f"Median:       {data_clean.median():.2f}    -->  {data.median():.2f}")
        print(f"Standard Deviation: {data_clean.std():.2f}    -->  {data.std():.2f}")
        print(f"Variance:      {data_clean.var():.2f}    -->  {data.var():.2f}")
        print(f"25th Percentile: {data_clean.quantile(0.25):.2f}    -->  {data.quantile(0.25):.2f}")
        print(f"50th Percentile: {data_clean.quantile(0.50):.2f}    -->  {data.quantile(0.50):.2f}")
        print(f"75th Percentile: {data_clean.quantile(0.75):.2f}    -->  {data.quantile(0.75):.2f}")
        print(f"N (observations): {len(data_clean)}    -->  {len(data)}")  # Shows difference in sample size


if __name__ == "__main__":
    for col in ratio_cols:
        summarise_ratio(col)
    for col in nominal_cols:
        summarise_nominal(col)
    for col in ordinal_cols:
        summarise_ordinal(col)
    for col in interval_cols:
        summarise_interval(col)