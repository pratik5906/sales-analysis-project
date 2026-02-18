import pandas as pd

df = pd.read_csv("cleaned_sales_data.csv")

# Total revenue
total_revenue = df['Sales'].sum()

# Total profit
total_profit = df['Profit'].sum()

# Profit margin
profit_margin = (total_profit / total_revenue) * 100

# Sales by category
category_sales = df.groupby('Category')['Sales'].sum()

# Profit by region
region_profit = df.groupby('Region')['Profit'].sum()

print("Total Revenue:", total_revenue)
print("Total Profit:", total_profit)
print("Profit Margin:", round(profit_margin,2), "%")

print("\nSales by Category:")
print(category_sales)

print("\nProfit by Region:")
print(region_profit)