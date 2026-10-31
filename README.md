# Corporate Financial Performance & Cost Intelligence

**Automotive Industry \| April 2024 -- March 2026**

## Project Overview

This project reviews the financial and manufacturing performance of a
simulated automotive business.

I used Python with Pandas for basic data inspection, cleaning, and
financial calculations. I used Tableau to create three dashboards that
present revenue, profit, manufacturing costs, and budget performance.

## Project Goals

-   Review revenue and operating profit.
-   Understand manufacturing costs.
-   Compare actual revenue and costs with budget figures.
-   Compare costs across car models and illustrative plants.
-   Estimate possible cost savings using a simple scenario.

## Tools Used

-   **Python** -- Basic data inspection, cleaning, and calculations.
-   **Pandas** -- Reading, checking, cleaning, and summarising tabular
    data.
-   **Tableau** -- Creating dashboards and charts.
-   **CSV** -- Storing the datasets and analysis outputs.

## How I Used Python

I used Python for a focused set of data tasks. This project does not
cover advanced Python programming or machine learning.

### 1. Data Inspection

I used these Pandas commands to understand the dataset:

  Command                   What it does
  ------------------------- ----------------------------------------------
  `pd.read_csv()`           Loads a CSV file into a DataFrame.
  `df.shape`                Shows the number of rows and columns.
  `df.head()`               Displays the first five rows.
  `df.columns.tolist()`     Shows the column names as a list.
  `df.info()`               Shows column data types and non-null counts.
  `df.isnull().sum()`       Counts missing values in each column.
  `df.duplicated().sum()`   Counts duplicate rows.

### 2. Data Cleaning

I used these Pandas commands to prepare the data:

  Command                  What it does
  ------------------------ -------------------------------------------
  `df.drop_duplicates()`   Removes duplicate rows.
  `df.dropna()`            Removes rows that contain missing values.
  `df.to_csv()`            Saves the cleaned data to a new CSV file.

### 3. Financial Calculations

I used basic Pandas calculations for the overall financial summary:

  --------------------------------------------------------------------------------
  Command or calculation                       What it does
  -------------------------------------------- -----------------------------------
  `df["Revenue_INR"].sum()`                    Adds the revenue values.

  `df["Total_Manufacturing_Cost_INR"].sum()`   Adds the manufacturing cost values.

  `df["Operating_Profit_INR"].sum()`           Adds the operating profit values.

  `(total_profit / total_revenue) * 100`       Calculates operating profit margin.

  `round(value, 2)`                            Rounds a result to two decimal
                                               places.
  --------------------------------------------------------------------------------

**Note:** The Python scripts supplied with this project use Pandas.
NumPy is not directly imported or used in these scripts, so it is not
listed as a project tool.

## Dataset

-   **Industry:** Automotive
-   **Period:** April 2024 to March 2026
-   **Records:** 480
-   **Columns:** 15
-   **Illustrative plants:** 4
-   **Car models:** 5
-   **Currency:** Indian Rupees (INR)

The dataset uses familiar car model and manufacturer names to make the
analysis easier to understand. The financial figures are synthetic and
were created for this learning project.

## Project Workflow

1.  **Data inspection:** Checked the dataset size, column names, data
    types, missing values, and duplicate rows.
2.  **Data cleaning:** Removed duplicate rows and rows with missing
    values, then saved the cleaned dataset.
3.  **Financial analysis:** Calculated total revenue, total
    manufacturing cost, total operating profit, and operating profit
    margin.
4.  **Dashboard development:** Used Tableau to present the results in
    three dashboards.

## Dashboards

### 1. Corporate Financial Performance & Cost Intelligence

An overall view of revenue, operating profit, manufacturing cost,
operating profit margin, and monthly revenue trends.

### 2. Manufacturing Cost & Plant Intelligence

A view of production versus sales, plant-wise manufacturing costs,
manufacturing costs by car model, and cost components.

### 3. Budget Variance & Cost Optimization

A comparison of actual and budget revenue and costs, revenue
achievement, and estimated savings under a hypothetical 5%
cost-reduction scenario.
## Dashboard Screenshots

### 1. Manufacturing Cost & Plant Intelligence
![Financial Overview](Dashboard%20Screenshots/Dashboard1.png)

### 2. Revenue & Profit Analysis
![Revenue & Profit Analysis](Dashboard%20Screenshots/Dashboard2.png)

### 3. Cost Analysis
![Cost Analysis](Dashboard%20Screenshots/dashboard%203.png)

## Key Measures

-   **Operating Profit:** Revenue minus total manufacturing cost, as
    defined for this project.
-   **Operating Profit Margin:** Operating profit divided by revenue,
    multiplied by 100.
-   **Revenue Variance:** Actual revenue minus budget revenue.
-   **Cost Variance:** Actual manufacturing cost minus budget cost.
-   **Estimated Cost Savings:** A scenario estimate based on a
    hypothetical 5% cost reduction.

## Project Files

The project folder contains the original and cleaned datasets, Python
scripts, analysis output files, dashboard screenshots, and Tableau
workbook files.

## Important Note

This is a synthetic educational project. It is not based on official or
audited financial data from Maruti Suzuki, Hyundai, Tata Motors,
Mahindra, or any other automotive company. Plant names and
model-to-plant assignments are illustrative. The analysis is a
simplified model and does not include every item used in real-world
financial accounting.

## What I Learned

-   Inspecting and cleaning tabular data with Python and Pandas.
-   Checking missing values and duplicate records.
-   Performing basic financial calculations.
-   Comparing actual results with budget benchmarks.
-   Building Tableau dashboards to communicate business information.
