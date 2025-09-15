import pandas as pd

# 1. Loader data
df = pd.read_csv("organizations-100.csv")

print("Original Data: ")
print(df)

# 2. Remove duplicates
df = df.drop_duplicates()
print(df)

# 3. Handle missing values
df["Index"] = df["Index"].fillna(df['Index'].mean()) # Replace missing values with the average
df["Country"] = df["Country"].fillna(df["Unkown"]) # Replace the mising values with unkown

# 4. Save Cleaned Data
df.to_excel("cleaned_organizations.xlsx",index=False)

print("\nCleaned Data Saved to 'cleaned_organizations.xlsx'")
print("Summary Report Saved to 'cleaned_organizations.xlsx'")

