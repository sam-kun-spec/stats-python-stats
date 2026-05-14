import pandas as pd
import numpy as np

# using our existing sales data
df = pd.read_csv('orders.csv')
df2 = pd.read_csv('products.csv')

df = pd.merge(df, df2, on='product_id', how='left')
df = df.dropna(subset=['customer_id'])
df['revenue'] = df['quantity'] * df['price']

print(df['revenue'].describe())
print()

# pracice shill by me;- 

# 1. Mean, Median, Mode
print("Mean:", df["revenue"].mean())
print("Median:", df["revenue"].median())
print("Mode:", df["revenue"].mode())

# 2. Variance and Std Dev
print("Variance:", df["revenue"].var())
print("Std Dev:", df["revenue"].std())

# 3. Skewness
print("Skewness:", df["revenue"].skew())

# 4. Percentiles
revenue_arr = df['revenue'].to_numpy()
print("Q1:", np.percentile(revenue_arr , 25))
print("Q2:", np.percentile(revenue_arr , 50))
print("Q3:", np.percentile(revenue_arr , 75))


# 5. IQR
iqr = np.percentile(revenue_arr , 75) - np.percentile(revenue_arr , 25)
print("IQR:", iqr)

# 6. Outlier detection
lower = (np.percentile(revenue_arr , 25)) - 1.5 * iqr
upper = (np.percentile(revenue_arr , 75)) + 1.5 * iqr 
outliers = df[(df['revenue'] < lower) | (df['revenue'] > upper)]
print("Outliers:", outliers.shape[0]) 