from data import df
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

if __name__ == "__main__":
    b1_result = b1_binning(n_bins=10)

    # saving to excel
    with pd.ExcelWriter('preprocessing_results.xlsx') as writer:
        b1_result.to_excel(writer, sheet_name='B1_Binning', index=False)

        print("\nBinning results saved to 'preprocessing_results.xlsx'")