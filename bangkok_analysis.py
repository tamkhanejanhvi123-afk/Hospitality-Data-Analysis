
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create output folder
os.makedirs("outputs", exist_ok=True)

# Load Airbnb dataset
df = pd.read_csv("data/bangkok_listings.csv", low_memory=False)
print("BANGKOK AIRBNB DATASET")

# Dataset overview
print("First Five Records:")
print(df.head())
print("Dataset Shape:")
print(df.shape)
print("Column Information:")
print(df.info())

# Data quality check
print("Missing Values:")
print(df.isnull().sum().sort_values(ascending=False).head(15))
print("Duplicate Records:")
print(df.duplicated().sum())

# Save data quality report
quality_report = pd.DataFrame({
    "Column": df.columns,
    "Missing_Values": df.isnull().sum().values,
    "Missing_Percentage": (
        df.isnull().mean().values * 100
    ).round(2)
})
quality_report.to_csv(
    "outputs/bangkok_data_quality.csv",
    index=False
)
# Convert price into numeric format
if "price" in df.columns:
    df["price"] = pd.to_numeric(
        df["price"].astype(str).str.replace(
            r"[$,]", "", regex=True
        ),
        errors="coerce"
    )
# Basic statistical analysis
print("Numerical Summary:")
print(df.describe())

df.describe(include="all").transpose().to_csv(
    "outputs/bangkok_statistical_summary.csv"
)
# Room type analysis
if "room_type" in df.columns:
    room_counts = df["room_type"].value_counts()

    print("Room Type Counts:")
    print(room_counts)

    room_counts.to_csv(
        "outputs/bangkok_room_types.csv"
    )

    plt.figure(figsize=(9, 5))
    sns.countplot(
        data=df,
        y="room_type",
        order=room_counts.index
    )
    plt.title("Airbnb Listings by Room Type")
    plt.xlabel("Number of Listings")
    plt.ylabel("Room Type")
    plt.tight_layout()
    plt.savefig("outputs/bangkok_room_types.png")
    plt.close()

# Price analysis
if "price" in df.columns:
    valid_prices = df[
        df["price"].notna() & (df["price"] > 0)
    ]
    print("Average Listing Price:")
    print(valid_prices["price"].mean())
    print("Median Listing Price:")
    print(valid_prices["price"].median())

    # Use the 99th percentile as the chart limit
    # to make the main price distribution easier to see
    if not valid_prices.empty:
        upper_limit = valid_prices["price"].quantile(0.99)

        plt.figure(figsize=(9, 5))
        sns.histplot(
            valid_prices[
                valid_prices["price"] <= upper_limit
            ]["price"],
            bins=30
        )
        plt.title("Bangkok Airbnb Price Distribution")
        plt.xlabel("Listing Price (dataset currency)")
        plt.ylabel("Number of Listings")
        plt.tight_layout()
        plt.savefig("outputs/bangkok_price_distribution.png")
        plt.close()

# Neighbourhood analysis
neighbourhood_column = next(
    (
        col for col in [
            "neighbourhood_cleansed",
            "neighbourhood"
        ]
        if col in df.columns
    ),
    None
)
if neighbourhood_column:
    top_neighbourhoods = (
        df[neighbourhood_column]
        .value_counts()
        .head(10)
    )
    print("Top 10 Neighbourhoods:")
    print(top_neighbourhoods)
    top_neighbourhoods.to_csv(
        "outputs/bangkok_top_neighbourhoods.csv"
    )
    plt.figure(figsize=(10, 6))
    sns.barplot(
        x=top_neighbourhoods.values,
        y=top_neighbourhoods.index
    )
    plt.title("Top 10 Bangkok Neighbourhoods by Listings")
    plt.xlabel("Number of Listings")
    plt.ylabel("Neighbourhood")
    plt.tight_layout()
    plt.savefig("outputs/bangkok_neighbourhoods.png")
    plt.close()

# Availability analysis
if "availability_365" in df.columns:
    print("Average Availability (Days):")
    print(df["availability_365"].mean())
print("ANALYSIS COMPLETED")
print("Check the outputs folder for reports and charts.")
