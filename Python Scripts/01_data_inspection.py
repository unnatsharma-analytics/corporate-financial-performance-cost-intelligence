
import pandas as pd

# 1. Load the dataset
df = pd.read_csv("data/automotive_financial_cost_intelligence_recognizable_models.csv")

# 2. Check dataset size
print("Dataset Shape:", df.shape)

# 3. View the first five records
print(df.head())

# 4. Check column names
print("Columns:", df.columns.tolist())

# 5. Check data types and non-null values
df.info()

# 6. Check missing values
print("Missing Values:\n", df.isnull().sum())

# 7. Check duplicate records
print("Duplicate Records:", df.duplicated().sum())
