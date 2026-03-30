from data import df
from sklearn.preprocessing import MinMaxScaler, StandardScaler, KBinsDiscretizer
import pandas as pd
import numpy as np

# B1 - Equi-width and Equi-depth Binning on Income

def b1_binning(n_bins=10):
    income = df['income'].dropna()  
    # pd.cut is used for equi-width binning, pd.qcut for equi-depth
    equi_width_bins = pd.cut(income, bins=n_bins)
    equi_depth_bins = pd.qcut(income, q=n_bins, duplicates='drop')  # Handle duplicate edges if not enough unique values

    print(f"Equi-width Binning (n_bins={n_bins}):")
    print(equi_width_bins.value_counts().sort_index())
    print(f"\nEqui-depth Binning (n_bins={n_bins}):")
    print(equi_depth_bins.value_counts().sort_index())

    result = pd.DataFrame({
        'income': income.values,
        'equi_width_bin': equi_width_bins.values, # takes range and divides equally -> equal range, unequal counts per bin
        'equi_depth_bin': equi_depth_bins.values  # takes total count and divides equally, equal counts, unequal range per bin
    })
    return result


def b2_normalisation():
    # b2 - Min-Max and Z-score Normalization on Loan Amount
    loan_amount = df[['loan_amount']] # Kept as dataframe through double brackets

    # Min-max Normalisation scales from 0 to 1
    minmax_scaler = MinMaxScaler()
    loan_minmax = minmax_scaler.fit_transform(loan_amount)

    # Z-score Normalisation scales values based on mean and standard deviation
    zscore_scaler = StandardScaler()
    loan_zscore = zscore_scaler.fit_transform(loan_amount)

    print("-" * 40)
    print("B2 - Loan Amount Normalisation:")
    print("-" * 40)
    print(f"\nOriginal   Min: {loan_amount.min().values[0]:.2f}, Max: {loan_amount.max().values[0]:.2f}")
    print(f"Min-Max    Min: {loan_minmax.min():.2f}, Max: {loan_minmax.max():.2f}")
    print(f"Z-Score    Mean: {loan_zscore.mean():.2f}, Std: {loan_zscore.std():.2f}")

    result = pd.DataFrame({
        'loan_amount': loan_amount.values.flatten(),
        'minmax_normalized': loan_minmax.flatten(),
        'zscore_normalized': loan_zscore.flatten()
    })

    return result



if __name__ == "__main__":
    b1_result = b1_binning(n_bins=10)
    b2_result = b2_normalisation()

    # saving to excel
    with pd.ExcelWriter('preprocessing_results.xlsx') as writer:
        b1_result.to_excel(writer, sheet_name='B1_Binning', index=False)
        b2_result.to_excel(writer, sheet_name='B2_Normalisation', index=False)

        print("\nBinning results saved to 'preprocessing_results.xlsx'")

