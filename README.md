# Hospitality Data Analysis

## Project Overview
This project performs an initial analysis of hotel booking data using Python. The dataset contains historical booking records for City Hotel and Resort Hotel.

The analysis focuses on:
- Understanding the dataset structure
- Checking missing values and duplicate records
- Cleaning selected missing values
- Calculating basic descriptive statistics
- Comparing hotel types and cancellation rates
- Reviewing monthly arrival counts and market segments
- Creating charts to present the findings

## Dataset
The project uses the **Hotel Booking Demand** dataset.

Dataset page:
https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand

Download the CSV file and save it here:

```text
data/hotel_bookings.csv
```

The dataset used in the analysis contains 119,390 rows and 32 columns.

## Project Folder Structure

```text
Hospitality_Data_Analysis/
│
├── data/
│   └── hotel_bookings.csv
│
├── outputs/
│   └── (generated reports, cleaned data and charts)
│
├── hospitality_analysis.py
├── README.md
└── requirements.txt
```

## Requirements
- Python 3
- pandas
- NumPy
- Matplotlib
- Seaborn

## Installation

Open a terminal in the project folder and run:

```bash
pip install -r requirements.txt
```

## Run the Project

Make sure `hotel_bookings.csv` is inside the `data` folder. Then run:

```bash
python hospitality_analysis.py
```

The script creates the `outputs` folder if it does not already exist and saves the analysis results there.

## Main Outputs
The script generates files such as:

- `initial_data_quality_report.csv` — missing-value and duplicate summary
- `duplicate_records.csv` — rows belonging to duplicate groups for review
- `cleaned_hotel_bookings.csv` — cleaned dataset
- `statistical_summary.csv` — descriptive statistics
- `hotel_type_counts.csv` — record counts by hotel type
- `cancellation_counts.csv` — canceled and not-canceled record counts
- `monthly_booking_counts.csv` — counts grouped by arrival month
- `hotel_wise_cancellation.csv` — cancellation percentages by hotel type
- `market_segment_counts.csv` — record counts by market segment
- PNG files — charts created by the script

## Initial Findings
Based on the dataset run used for this project:

- Total records: 119,390
- Total columns: 32
- City Hotel records: 79,330
- Resort Hotel records: 40,060
- Canceled bookings: 44,224 (approximately 37.04%)
- Average daily rate (ADR): approximately 101.83 in the dataset's recorded units
- City Hotel cancellation percentage: approximately 41.73%
- Resort Hotel cancellation percentage: approximately 27.76%
- Online TA is the largest market segment in the dataset.

These are findings from the historical dataset used in this project. They should not be treated as current hotel-market statistics.

## Notes on Data Cleaning
The analysis fills missing values in selected columns:
- `children` with `0`
- `country` with `Unknown`
- `agent` with `0`
- `company` with `0`

The duplicate rows are exported for review rather than automatically deleted. Identical values across the available columns do not always prove that records represent the same real-world booking.

## Project Status
This project covers the initial analysis of one public hotel-booking dataset. A second public hospitality dataset may be added in a later stage; it should only be described as analysed after it has actually been downloaded and processed.
