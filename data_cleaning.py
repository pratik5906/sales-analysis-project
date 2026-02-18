import pandas as pd

# Load raw data
df = pd.read_csv("sales_data.csv")

print("Original Shape:", df.shape)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Handle missing values (if any)
df.fillna(0, inplace=True)

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

# Create Month column
df['Month'] = df['Date'].dt.month

# Save cleaned dataset
df.to_csv("cleaned_sales_data.csv", index=False)

print("Cleaned dataset saved successfully!")