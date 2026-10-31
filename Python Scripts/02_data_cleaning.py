
import pandas as pd

# 1. Load the dataset
df = pd.read_csv("data/automotive_financial_cost_intelligence_recognizable_models.csv")

# 2. Remove duplicate records
df = df.drop_duplicates()

# 3. Check missing values
print("Missing Values Before Cleaning:")
print(df.isnull().sum())

# 4. Remove rows with missing values
df = df.dropna()

# 5. Save the cleaned dataset
df.to_csv("outputs/cleaned_automotive_data.csv", index=False)

# 6. Check the final dataset
print("\nCleaned Dataset Shape:", df.shape)
print("Duplicate Records:", df.duplicated().sum())
print("Missing Values Remaining:", df.isnull().sum().sum())
