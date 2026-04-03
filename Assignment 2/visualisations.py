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

def plot_nominal(col):

    data = df[col]
    data_clean = data.dropna()

    if col in missing_cols:
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        fig.suptitle(f'{col} - With vs Without Missing Values', fontsize=14)

        #Include Missing Values
        freq_with = data.value_counts(dropna=False) 
        sns.barplot(x=freq_with.index.astype(str), y=freq_with.values, ax=axes[0], color='steelblue')
        axes[0].set_title('Frequency (Including Missing Values)')
        axes[0].set_xlabel(col)
        axes[0].set_ylabel('Count')

        #Exclude Missing Values
        freq_without = data_clean.value_counts()
        sns.barplot(x=freq_without.index.astype(str), y=freq_without.values, ax=axes[1], color='salmon')
        axes[1].set_title('Frequency (Excluding Missing Values)')
        axes[1].set_xlabel(col)
        axes[1].set_ylabel('Count')

    else:
        # Normal Bar Chart
        fig, axes = plt.subplots(figsize=(10, 5))
        freq = data.value_counts(dropna=False)
        sns.barplot(x=freq.index.astype(str), y=freq.values, ax=axes, color='steelblue')
        axes.set_title('Frequency')
        axes.set_xlabel(col)
        axes.set_ylabel('Count')

    plt.tight_layout()
    plt.show()

def plot_ordinal(col):
    
    data = df[col]
    data_clean = data.dropna()

    if pd.api.types.is_datetime64_any_dtype(df[col]):
        data_period = data.dt.to_period('M')  # Convert to monthly periods for better visualization
        data_clean_period = data_clean.dt.to_period('M')

        freq = data_period.value_counts().sort_index()
        
        fig, axes = plt.subplots(figsize=(12, 6))
        sns.lineplot(x=freq.index.astype(str), y=freq.values, marker='o', ax=axes, color='steelblue')
        axes.set_title(f'Frequency of {col} Over Time')
        axes.set_xlabel(col)
        axes.set_ylabel('Count')
        plt.tight_layout()
        plt.show()
        return


    if col in missing_cols:
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        fig.suptitle(f'{col} - With vs Without Missing Values', fontsize=14)

        # Include Missing Values
        freq_with = data.value_counts(dropna=False)
        sns.barplot(x=freq_with.index.astype(str), y=freq_with.values, ax=axes[0], color='steelblue')
        axes[0].set_title('Frequency (Including Missing Values)')
        axes[0].set_xlabel(col)
        axes[0].set_ylabel('Count')

        # Exclude Missing Values
        freq_without = data_clean.value_counts()
        sns.barplot(x=freq_without.index.astype(str), y=freq_without.values, ax=axes[1], color='salmon')
        axes[1].set_title('Frequency (Excluding Missing Values)')
        axes[1].set_xlabel(col)
        axes[1].set_ylabel('Count')

    else:
        # Normal Bar Chart
        fig, axes = plt.subplots(figsize=(10, 5))
        freq = data.value_counts(dropna=False)
        sns.barplot(x=freq.index.astype(str), y=freq.values, ax=axes, color='steelblue')
        axes.set_title('Frequency')
        axes.set_xlabel(col)
        axes.set_ylabel('Count')

    plt.tight_layout()
    plt.show()

def plot_interval(col):
    data = df[col]
    data_clean = data.dropna()

    if col in missing_cols:
        # 2x2 for Histogram and Boxplot 
        fig, axes = plt.subplots(2, 2, figsize=(12, 8))
        fig.suptitle(f'{col} - With vs Without Missing Values', fontsize=14)

        # Include Missing Values
        sns.histplot(data, bins=30, kde=True, ax=axes[0, 0], color='steelblue')
        axes[0, 0].set_title('Histogram (Including Missing Values)')
        axes[0, 0].set_xlabel(col)
        axes[0, 0].set_ylabel('Frequency')

        # Exclude Missing Values
        sns.histplot(data_clean, bins=30, kde=True, ax=axes[0, 1], color='salmon')
        axes[0, 1].set_title('Histogram (Excluding Missing Values)')
        axes[0, 1].set_xlabel(col)
        axes[0, 1].set_ylabel('Frequency')

        # Boxplots
        sns.boxplot(x=data, ax=axes[1, 0], color='steelblue')
        axes[1, 0].set_title('Boxplot (Including Missing Values)')
        axes[1, 0].set_xlabel(col)

        sns.boxplot(x=data_clean, ax=axes[1, 1], color='salmon')
        axes[1, 1].set_title('Boxplot (Excluding Missing Values)')
        axes[1, 1].set_xlabel(col)

    else:
        # 1 x 2 grid for Histogram and Boxplot
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

def plot_correlation_heatmap():
    # only numeric columns for correlation
    numeric_df = df.select_dtypes(include=['number'])

    plt.figure(figsize=(14, 10))
    sns.heatmap(numeric_df.corr(), annot=True, fmt=".2f", cmap='coolwarm', center = 0,linewidths=0.5)
    plt.title('Correlation Heatmap of Numeric Attributes', fontsize=16)
    plt.tight_layout()
    plt.show()

def plot_clustering():
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    fig.suptitle('Clustering Analysis', fontsize=14)

    #cluster 1 - income vs monthly expenses
    sns.scatterplot(
        data = df,
        x='income',
        y='monthly_expenses',
        ax=axes[0],
        alpha = 0.5,
        color = 'steelblue'
    )

    axes[0].set_title('Income vs Monthly Expenses')
    axes[0].set_xlabel('Income')
    axes[0].set_ylabel('Monthly Expenses')

    #cluster 2 - credit score vs debt to income coloured by loan default
    sns.scatterplot(
        data = df,
        x='credit_score',
        y='debt_to_income_pct',
        hue='loan_default',
        ax=axes[1],
        alpha = 0.5,
        palette = {0: 'steelblue', 1: 'salmon'}
    )
    axes[1].set_title('Credit Score vs Debt to Income (by Loan Default)')
    axes[1].set_xlabel('Credit Score')
    axes[1].set_ylabel('Debt to Income')
    axes[1].legend(title = 'Loan Default', labels=['No Default', 'Default'])

    plt.tight_layout()
    plt.show()


def plot_outliers():
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    fig.suptitle('Outlier Detection - Income', fontsize=14)

    #boxplot
    sns.boxplot(x=df['income'], ax=axes[0], color='steelblue')
    axes[0].set_title('Boxplot of Income')
    axes[0].set_xlabel('Income')

    #IQR outlier detection
    Q1 = df['income'].quantile(0.25)
    Q3 = df['income'].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    outliers = df[(df['income'] < lower) | (df['income'] > upper)]['income']

    print(f"IQR: {IQR:.2f}")
    print(f"Lower Bound: {lower:.2f}")
    print(f"Upper Bound: {upper:.2f}")
    print(f"Number of Outliers: {len(outliers)}")
    print(f"Outlier min: {outliers.min():.2f}")
    print(f"Outlier max: {outliers.max():.2f}")

    #Historgram that displays outliers
    sns.histplot(df['income'], bins=30, kde=True, ax=axes[1], color='salmon')
    axes[1].set_title('Income Distribution with Outliers')
    axes[1].axvline(lower, color='red', linestyle='--', label=f'Lower Bound: {lower:.2f}')
    axes[1].axvline(upper, color='red', linestyle='--', label=f'Upper Bound: {upper:.2f}')
    axes[1].set_xlabel('Income')
    axes[1].set_ylabel('Frequency')
    axes[1].legend()

    plt.tight_layout()
    plt.show()

def plot_patterns():
    fig, axes = plt.subplots(1, 3, figsize=(14, 5))
    fig.suptitle('Pattern Analysis', fontsize=14)

    #pattern 1 - credit score vs loan default
    sns.boxplot(
        data = df,
        x='loan_default',
        y='credit_score',
        ax=axes[0],
        color = 'steelblue'
    )

    axes[0].set_title('Credit Score by Loan Default')
    axes[0].set_xlabel('Loan Default (0 = No Default, 1 = Default)')
    axes[0].set_ylabel('Credit Score')

    #pattern 2 - debt to income vs loan default
    sns.boxplot(
        data = df,
        x='loan_default',
        y='debt_to_income_pct',
        ax=axes[1],
        color='salmon'
    )

    axes[1].set_title('Debt to Income % by Loan Default')
    axes[1].set_xlabel('Loan Default (0 = No Default, 1 = Default)')
    axes[1].set_ylabel('Debt to Income')

    #pattern 3 - loan amount vs loan default
    sns.boxplot(
        data = df,
        x='loan_default',
        y='loan_amount',
        ax=axes[2],
        color='steelblue'
    )

    axes[2].set_title('Loan Amount by Loan Default')
    axes[2].set_xlabel('Loan Default (0 = No Default, 1 = Default)')
    axes[2].set_ylabel('Loan Amount')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    for col in ratio_cols:
        plot_ratio(col)
    for col in nominal_cols:
        plot_nominal(col)
    for col in ordinal_cols:
        plot_ordinal(col)
    for col in interval_cols:
        plot_interval(col)
    plot_correlation_heatmap()
    plot_clustering()
    plot_outliers()
    plot_patterns()
