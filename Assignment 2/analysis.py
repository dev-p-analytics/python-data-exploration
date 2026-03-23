from data import df, ratio_cols, nominal_cols, ordinal_cols, interval_cols, missing_cols

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

def summarise_nominal(col):
    print("-" * 40)
    print(f"\nSummary for: {col}")
    print("-" * 40)

    data = df[col]
    data_clean = data.dropna()  # Remove missing values for summary statistics

    #frequency and relative frequency
    freq = data.value_counts()
    rel_freq = data.value_counts(normalize=True) * 100

    print(f"Mode: {data.mode().iloc[0]}")
    print(f"Missing Values: {data.isnull().sum()}")

    if col in missing_cols:
        print(f"\n                   Without Missing  -->  With Missing")
        print(f"\nMode:              {data_clean.mode().iloc[0]}    -->  {data.mode().iloc[0]}")
        for category in freq.index:
            print(f"{category}: {data_clean.value_counts()[category]} ({data_clean.value_counts(normalize=True)[category] * 100:.2f}%)    -->  {freq[category]} ({rel_freq[category]:.2f}%)")
    else:
        for category in freq.index:
            print(f"{category}: {freq[category]} ({rel_freq[category]:.2f}%)")

if __name__ == "__main__":
    for col in ratio_cols:
        summarise_ratio(col)
    for col in nominal_cols:
        summarise_nominal(col)

