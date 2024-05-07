import pandas as pd

# Load the two CSV files
df1 = pd.read_csv('973predictions.csv')
df2 = pd.read_csv('predictions.csv')

# Ensure the same order of columns for comparison
df2 = df2[df1.columns]

# Compare the two dataframes
comparison_df = df1.eq(df2)

# If all values in a row are True, the rows are identical
identical_rows = comparison_df.all(axis=1)

# Print out the result
print(f'Number of identical rows: {identical_rows.sum()}')
print(f'Total rows: {len(df1)}')
