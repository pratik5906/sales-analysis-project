# Retail Sales Analysis Dashboard

## Project Overview

This is an end-to-end retail sales analytics project where synthetic sales data was generated, cleaned, analyzed, and visualized to derive meaningful business insights.

The goal of this project was to simulate a real-world retail environment and perform category-level and regional performance analysis using Python and Tableau.

---

## Objectives

- Generate realistic multi-category retail sales data
- Perform data cleaning and preprocessing
- Conduct exploratory data analysis (EDA)
- Calculate key performance indicators (KPIs)
- Analyze revenue, profitability, and margin trends
- Build an interactive Tableau dashboard

---

## Tech Stack

- Python (Pandas, NumPy)
- Tableau Public
- Git & GitHub

---

## Project Structure

Sales-Analysis-Project/
│
├── sales_data_generator.py
├── data_cleaning.py
├── analysis.py
├── sales_data.csv
├── cleaned_sales_data.csv
├── Retail_Sales_Dashboard.twbx
└── README.md

---

## Project Workflow

1. Data Generation
- Created synthetic retail sales dataset using NumPy and Pandas
- Included fields like Order ID, Date, Category, Region, Sales, Profit, Quantity, Discount

2. Data Cleaning
- Removed duplicates
- Handled missing values
- Converted Date column to datetime format
- Created derived Month column

3. Exploratory Data Analysis (EDA)
- Calculated Total Revenue
- Calculated Total Profit
- Calculated Profit Margin
- Aggregated Sales by Category
- Aggregated Profit by Region
- Analyzed Monthly Revenue Trends

Used Pandas groupby() operations for aggregation.

---

## Key Business Insights

- Grocery category generated the highest total revenue.
- Fashion category showed the highest profit margin.
- North region delivered the strongest profitability.
- Sales trends fluctuated seasonally across months.
- High revenue categories did not always produce the highest margins.

---

## Dashboard Features

- KPI Section:
  - Total Revenue
  - Total Profit
  - Quantity Sold
  - Profit Margin

- Visualizations:
  - Sales by Category
  - Monthly Sales & Profit Trend
  - Profit by Region
  - Profit Margin by Category

- Interactive Filters:
  - Category
  - Region

---

## How to Run

Generate Dataset:
python3 sales_data_generator.py

Clean Data:
python3 data_cleaning.py

Run Analysis:
python3 analysis.py

---

## Live Dashboard

(Add your Tableau Public link here)

---

## Author

Pratik Kumar  
Aspiring Data Analyst | Python & GenAI Enthusiast  
GitHub: https://github.com/pratik5906
