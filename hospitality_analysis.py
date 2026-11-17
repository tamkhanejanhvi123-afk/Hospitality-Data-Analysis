import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 2. Create Output Folder
os.makedirs("outputs", exist_ok=True)
sns.set_theme(style="whitegrid")

# 3. Load Dataset
df = pd.read_csv("data/hotel_bookings.csv")
print("DATASET LOADED SUCCESSFULLY")
print("First Five Records:")
print(df.head())
print("Dataset Information:")
df.info()
print("Rows and Columns:")
print(df.shape)

# 4. Initial Data Quality Assessment
print("INITIAL DATA QUALITY")
print("Missing Values:")
print(df.isnull().sum())
print("Duplicate Records:")
print(df.duplicated().sum())

# Save initial data quality report
missing = df.isnull().sum()
missing_percentage = (missing / len(df)) * 100
quality_report = pd.DataFrame({
    "Missing_Values": missing,
    "Missing_Percentage": missing_percentage
})
quality_report.to_csv(
    "outputs/initial_data_quality_report.csv"
)
print("Initial Data Quality Report:")
print(quality_report)

# 5. Inspect Duplicate Records
duplicate_data = df[df.duplicated(keep=False)]
print("DUPLICATE RECORD ANALYSIS")
print("First 10 Duplicate Records:")
print(duplicate_data.head(10))
print("Total Duplicate Records:")
print(df.duplicated().sum())
print("Duplicate Records by Hotel Type:")
print(duplicate_data["hotel"].value_counts())

# Save duplicate records for further investigation
duplicate_data.to_csv(
    "outputs/duplicate_records.csv",
    index=False
)
# Important:
# Duplicate rows are inspected but NOT automatically deleted.
# Different reservations can sometimes have identical values.
# 6. Handle Missing Values
print("DATA CLEANING")
# Fill missing children values with 0
df["children"] = df["children"].fillna(0)
# Fill missing country values with Unknown
df["country"] = df["country"].fillna("Unknown")
# Fill missing agent IDs with 0
df["agent"] = df["agent"].fillna(0)
# Fill missing company IDs with 0
df["company"] = df["company"].fillna(0)

print("Missing Values After Cleaning:")
print(df.isnull().sum())

# 7. Convert Reservation Date into Datetime
df["reservation_status_date"] = pd.to_datetime(
    df["reservation_status_date"],
    errors="coerce"
)
print("Updated Data Types:")
print(df.dtypes)
print("Invalid Reservation Dates:")
print(df["reservation_status_date"].isnull().sum())

# 8. Save Cleaned Dataset
df.to_csv(
    "outputs/cleaned_hotel_bookings.csv",
    index=False
)
print("Cleaned dataset saved successfully.")

# 9. Statistical Summary
print("STATISTICAL SUMMARY")
summary = df.describe(include="all")
print(summary)
summary.to_csv("outputs/statistical_summary.csv")

# 10. Hotel Type Analysis
print("HOTEL TYPE ANALYSIS")
hotel_counts = df["hotel"].value_counts()
print("Hotel Type Count:")
print(hotel_counts)
hotel_counts.to_csv("outputs/hotel_type_counts.csv")

# 11. Cancellation Analysis
print("CANCELLATION ANALYSIS")
cancellation_counts = df["is_canceled"].value_counts()
print("Cancellation Count:")
print(cancellation_counts)
cancellation_rate = df["is_canceled"].mean() * 100
print("Cancellation Rate:")
print(round(cancellation_rate, 2), "%")
cancellation_counts.to_csv(
    "outputs/cancellation_counts.csv"
)

# 12. Average Daily Rate Analysis
print("AVERAGE DAILY RATE")
average_adr = df["adr"].mean()
print("Average Daily Rate:")
print(round(average_adr, 2))

# 13. Monthly Booking Analysis
print("MONTHLY BOOKING ANALYSIS")
month_order = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]
monthly = df["arrival_date_month"].value_counts()
monthly = monthly.reindex(month_order, fill_value=0)
print("Monthly Booking Counts:")
print(monthly)
monthly.to_csv("outputs/monthly_booking_counts.csv")

# 14. Hotel-wise Cancellation Analysis
print("HOTEL-WISE CANCELLATION")
hotel_cancellation = (
    df.groupby("hotel")["is_canceled"].mean() * 100
)
print("Cancellation Percentage by Hotel:")
print(hotel_cancellation.round(2))
hotel_cancellation.to_csv(
    "outputs/hotel_wise_cancellation.csv"
)

# 15. Market Segment Analysis
print("MARKET SEGMENT ANALYSIS")
market_counts = df["market_segment"].value_counts()
print("Bookings by Market Segment:")
print(market_counts)
market_counts.to_csv(
    "outputs/market_segment_counts.csv"
)

# 16. DATA VISUALIZATION
# Chart 1: Bookings by Hotel Type
plt.figure(figsize=(8, 5))
sns.countplot(
    data=df,
    x="hotel",
    hue="hotel",
    legend=False
)
plt.title("Bookings by Hotel Type")
plt.xlabel("Hotel Type")
plt.ylabel("Number of Bookings")
plt.tight_layout()
plt.savefig("outputs/hotel_types.png")
plt.show()

# Chart 2: Booking Cancellation Analysis
plt.figure(figsize=(8, 5))
sns.countplot(
    data=df,
    x="is_canceled",
    hue="is_canceled",
    legend=False
)
plt.title("Hotel Booking Cancellation Analysis")
plt.xlabel("Cancellation (0 = No, 1 = Yes)")
plt.ylabel("Number of Bookings")
plt.tight_layout()
plt.savefig("outputs/cancellations.png")
plt.show()

# Chart 3: Average Daily Rate Distribution
plt.figure(figsize=(8, 5))
sns.histplot(
    df["adr"].dropna(),
    bins=40,
    kde=True
)
plt.title("Distribution of Average Daily Rates")
plt.xlabel("Average Daily Rate")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("outputs/average_daily_rate.png")
plt.show()

# Chart 4: Monthly Booking Trends
plt.figure(figsize=(10, 5))
sns.barplot(
    x=monthly.index,
    y=monthly.values
)
plt.title("Monthly Hotel Booking Trends")
plt.xlabel("Arrival Month")
plt.ylabel("Number of Booking Records")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/monthly_booking_trend.png")
plt.show()

# Chart 5: Cancellation Percentage by Hotel Type
plt.figure(figsize=(8, 5))
sns.barplot(
    x=hotel_cancellation.index,
    y=hotel_cancellation.values
)
plt.title("Cancellation Percentage by Hotel Type")
plt.xlabel("Hotel Type")
plt.ylabel("Cancellation Percentage (%)")
plt.tight_layout()
plt.savefig("outputs/hotel_wise_cancellation.png")
plt.show()

# Chart 6: Bookings by Market Segment
plt.figure(figsize=(10, 5))
sns.barplot(
    x=market_counts.index,
    y=market_counts.values
)
plt.title("Bookings by Market Segment")
plt.xlabel("Market Segment")
plt.ylabel("Number of Bookings")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/market_segment.png")
plt.show()

# 17. FINAL ANALYSIS SUMMARY
print("FINAL ANALYSIS SUMMARY")
print("Total Booking Records:", len(df))
print("Total Columns:", len(df.columns))
print("City Hotel Bookings:",
      hotel_counts.get("City Hotel", 0))
print("Resort Hotel Bookings:",
      hotel_counts.get("Resort Hotel", 0))
print("Total Duplicate Records Inspected:",
      len(duplicate_data))
print("Cancellation Rate:",
      round(cancellation_rate, 2), "%")
print("Average Daily Rate:",
      round(average_adr, 2))
print("Highest Arrival Month:",
      monthly.idxmax())
print("Lowest Arrival Month:",
      monthly.idxmin())
print("All reports and charts are saved in the outputs folder.")
print("ANALYSIS COMPLETED SUCCESSFULLY")
