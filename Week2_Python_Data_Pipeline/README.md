
# Python Data Pipeline for Hospitality Analytics

## Project Overview

This project focuses on designing and implementing a Python-based data pipeline for hospitality data analysis.

The pipeline uses two publicly available datasets:
- Hotel Booking Demand Dataset
- Bangkok Airbnb Listings Dataset

The main objective is to load, inspect, clean and store hospitality datasets using Python.

## Datasets Used

### 1. Hotel Booking Demand Dataset
- Contains 119,390 records.
- Includes hotel booking information such as hotel type, arrival dates, customer details, and booking status.
- Used to understand hotel booking patterns.

### 2. Bangkok Airbnb Listings Dataset
- Contains 30,922 records.
- Includes Airbnb listing information such as property details, location, prices and availability.
- Used to understand accommodation listings.

## Technologies and Libraries

- Python
- Pandas
- NumPy
- CSV
- Logging

## Pipeline Workflow

1. Data Ingestion – Load datasets from CSV files.
2. Data Inspection – Examine records, columns and missing values.
3. Data Cleaning – Identify and remove duplicate records.
4. Data Transformation – Standardize column names.
5. Data Validation – Check the processed dataset structure.
6. Data Storage – Save processed datasets as CSV files.

## Project Structure

```text
Week2_Python_Data_Pipeline/
│
├── data/
├── output/
├── pipeline.py
├── pipeline.log
├── README.md
└── requirements.txt
```

## Output Files

- hotel_bookings_cleaned.csv
- bangkok_listings_cleaned.csv

## Execution

Run the following command:

```bash
python pipeline.py
```

## Learning Outcomes

Through this project, I learned how to load large datasets, inspect missing values, identify duplicate records, process data using Pandas and save cleaned datasets. I also gained practical knowledge of logging and basic error handling in Python.

## Conclusion

This project demonstrates a basic Python data pipeline for hospitality analytics. It provides a structured approach to processing hospitality datasets and preparing them for further analysis.
