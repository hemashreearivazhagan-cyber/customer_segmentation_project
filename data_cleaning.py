# ==========================================
# CUSTOMER SEGMENTATION
# DATA CLEANING & PREPROCESSING
# ==========================================

import os
import pandas as pd

# ==========================================
# PROJECT PATHS
# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_FILE = os.path.join(
    BASE_DIR,
    "Mall_Customers.csv",
    "data",
    "Mall_Customers.csv"
)

OUTPUT_DIR = os.path.join(BASE_DIR, "output")

os.makedirs(OUTPUT_DIR, exist_ok=True)

OUTPUT_FILE = os.path.join(
    OUTPUT_DIR,
    "cleaned_mall_customers.csv"
)

# ==========================================
# LOAD DATASET
# ==========================================

print("=" * 50)
print("Loading Dataset...")
print("=" * 50)

df = pd.read_csv(DATA_FILE)

print("Dataset Loaded Successfully!\n")

# ==========================================
# DISPLAY FIRST 5 ROWS
# ==========================================

print("First 5 Rows")
print(df.head())

# ==========================================
# DATASET INFORMATION
# ==========================================

print("\n" + "=" * 50)
print("Dataset Information")
print("=" * 50)

print(df.info())

# ==========================================
# DATASET SHAPE
# ==========================================

print("\nDataset Shape:", df.shape)

# ==========================================
# CHECK MISSING VALUES
# ==========================================

print("\n" + "=" * 50)
print("Missing Values")
print("=" * 50)

print(df.isnull().sum())

# ==========================================
# REMOVE DUPLICATES
# ==========================================

duplicates = df.duplicated().sum()

print("\nDuplicate Rows:", duplicates)

df = df.drop_duplicates()

# ==========================================
# STANDARDIZE TEXT
# ==========================================

df["Gender"] = (
    df["Gender"]
    .str.strip()
    .str.title()
)

# ==========================================
# RENAME COLUMNS
# ==========================================

df.columns = [
    "CustomerID",
    "Gender",
    "Age",
    "Annual_Income",
    "Spending_Score"
]

# ==========================================
# CHECK DATA TYPES
# ==========================================

print("\n" + "=" * 50)
print("Data Types")
print("=" * 50)

print(df.dtypes)

# ==========================================
# SUMMARY STATISTICS
# ==========================================

print("\n" + "=" * 50)
print("Summary Statistics")
print("=" * 50)

print(df.describe())

# ==========================================
# SAVE CLEANED DATASET
# ==========================================

df.to_csv(OUTPUT_FILE, index=False)

# ==========================================
# SUCCESS MESSAGE
# ==========================================

print("\n" + "=" * 50)
print("Data Cleaning Completed Successfully!")
print("=" * 50)

print("Cleaned dataset saved at:")
print(OUTPUT_FILE)