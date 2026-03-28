from data import df, ratio_cols, nominal_cols, ordinal_cols, interval_cols, missing_cols
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_ratio(col):
    data = df[col]
    data_clean = data.dropna()

    if col in missing_cols:
        # 2x2 Grid - Histogram and Boxplot with and without missing values
        fig, axes = plt.subplots(2, 2, figsize=(12, 8))
        fig.suptitle(f'{col} - With vs Without Missing Values', fontsize=14)

        # Histograms
        sns.histplot(data, bins=30, kde=True, ax=axes[0, 0], color='steelblue')
        axes[0, 0].set_title('Histogram (Including Missing)')
        axes[0, 0].set_xlabel(col)
        axes[0, 0].set_ylabel('Frequency')

        sns.histplot(data_clean, bins=30, kde=True, ax=axes[0, 1], color='steelblue')
        axes[0, 1].set_title('Histogram (Excluding Missing)')
        axes[0, 1].set_xlabel(col)
        axes[0, 1].set_ylabel('Frequency')

        # Boxplots
        sns.boxplot(x=data, ax=axes[1, 0], color='salmon')
        axes[1, 0].set_title('Boxplot (Including Missing)')
        axes[1, 0].set_xlabel(col)

        sns.boxplot(x=data_clean, ax=axes[1, 1], color='salmon')
        axes[1, 1].set_title('Boxplot (Excluding Missing)')
        axes[1, 1].set_xlabel(col)
    
    else:
        # 1x2 Grid - Histogram and Boxplot
        fig, axes = plt.subplots(1, 2, figsize=(12, 4))
        fig.suptitle(f'{col}', fontsize=14)

        sns.histplot(data, bins=30, kde=True, ax=axes[0], color='steelblue')
        axes[0].set_title('Histogram')
        axes[0].set_xlabel(col)
        axes[0].set_ylabel('Frequency')

        sns.boxplot(y=data, ax=axes[1], color='salmon')
        axes[1].set_title('Boxplot')
        axes[1].set_ylabel(col)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    for col in ratio_cols:
        plot_ratio(col)