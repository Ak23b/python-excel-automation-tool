
# 📊 Organizations Dataset Analysis

# This notebook analyzes the organizations dataset with 100 entries, focusing on countries, industries, founding years, and employee sizes.

## 1. Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("organizations-100.csv")

# Setup styles
sns.set_theme(style="whitegrid")  # clean Seaborn style

## 2. Overview of Dataset
print("Shape:", df.shape)
print("\nColumns:", df.columns)
print("\nInfo:")
print(df.info())
print("\nFirst rows:")
print(df.head())

## 3. Founding Year Distribution
plt.figure(figsize=(10,5))
sns.histplot(df['Founded'], bins=20, kde=True)
plt.title("Distribution of Founding Years")
plt.xlabel("Year Founded")
plt.ylabel("Count")
plt.show()

## 4. Employee Size Distribution
plt.figure(figsize=(10,5))
sns.histplot(df['Number of employees'], bins=20, kde=True)
plt.title("Distribution of Number of Employees")
plt.xlabel("Employees")
plt.ylabel("Count")
plt.show()

## 5. Top 10 Countries by Number of Organizations
plt.figure(figsize=(12,6))
top_countries = df['Country'].value_counts().head(10)
sns.barplot(x=top_countries.values, y=top_countries.index)
plt.title("Top 10 Countries by Number of Organizations")
plt.xlabel("Count")
plt.ylabel("Country")
plt.show()

## 6. Top 10 Industries
plt.figure(figsize=(12,6))
top_industries = df['Industry'].value_counts().head(10)
sns.barplot(x=top_industries.values, y=top_industries.index)
plt.title("Top 10 Industries")
plt.xlabel("Count")
plt.ylabel("Industry")
plt.show()


## 7. Employees by Industry (Boxplot)
plt.figure(figsize=(12,6))
sns.boxplot(data=df, x='Industry', y='Number of employees')
plt.xticks(rotation=90)
plt.title("Employee Distribution by Industry")
plt.show()

