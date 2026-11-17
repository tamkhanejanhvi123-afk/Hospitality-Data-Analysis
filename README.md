
# Hospitality Data Analysis

## Project Overview

This project focuses on collecting, cleaning, and analysing hospitality-related data using Python. The main objective is to understand hotel booking patterns, cancellations, room types, accommodation prices, and neighbourhood-level listing distribution.

Two public datasets have been used for this project:
1. Hotel Booking Demand Dataset
2. Inside Airbnb Bangkok Listings Dataset

## Tools and Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter/VS Code
- Git and GitHub

## Datasets Used

### 1. Hotel Booking Demand Dataset

**Source:** https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand

- Records: 119,390
- Columns: 32
- Contains booking information for City Hotels and Resort Hotels.
- Includes booking dates, cancellations, customer details, market segments, and average daily rates.

**Analysis Performed:**
- Checked missing values and duplicate records.
- Cleaned selected missing values.
- Analysed hotel types and cancellation patterns.
- Calculated cancellation percentages.
- Studied monthly booking arrivals.
- Analysed market segments and average daily rates.
- Created charts to understand booking trends.

**Key Findings:**
- City Hotel bookings: 79,330
- Resort Hotel bookings: 40,060
- Total cancellations: 44,224
- Overall cancellation rate: 37.04%
- City Hotel cancellation rate: 41.73%
- Resort Hotel cancellation rate: 27.76%
- August recorded the highest number of arrivals in the combined monthly analysis.
- Online Travel Agents were the largest market segment.

### 2. Inside Airbnb Bangkok Listings Dataset

**Source:** https://insideairbnb.com/get-the-data/

- Location: Bangkok, Thailand
- Records: 30,922
- Columns: 90
- Contains short-term accommodation listing information, room types, prices, neighbourhoods, reviews, and availability.

**Analysis Performed:**
- Checked missing values and duplicate records.
- Converted price values into numeric format for analysis.
- Analysed room type distribution.
- Calculated average and median listing prices.
- Identified neighbourhoods with the highest number of listings.
- Analysed listing availability.
- Created visualisations for room types, prices, and neighbourhoods.

**Key Findings:**
- Total listings: 30,922
- Duplicate records: 0
- Missing price values: 2,259
- Entire home/apartment: 20,811
- Private room: 9,270
- Shared room: 551
- Hotel room: 290
- Average listing price: 2,910.87
- Median listing price: 1,601.33
- Average availability: approximately 272 days.
- Vadhana had the highest number of listings, with 4,486.

*Note: The listing dataset represents accommodation listings, not confirmed reservations or actual occupancy. The price currency/unit has not been independently confirmed.*

## Data Cleaning and Quality Checks

The following data quality checks were performed:

- Identified missing values.
- Checked duplicate records.
- Converted selected columns into appropriate data types.
- Handled selected missing values in the hotel booking dataset.
- Converted price values into numeric format in the Bangkok listings dataset.
- Generated data quality reports for both datasets.

Duplicate hotel booking records were identified and exported for review rather than automatically deleting them.

## Project Structure

```text
Hospitality_Data_Analysis/
│
├── data/
│   ├── hotel_bookings.csv
│   └── bangkok_listings.csv
│
├── outputs/
│   ├── initial_data_quality_report.csv
│   ├── duplicate_records.csv
│   ├── cleaned_hotel_bookings.csv
│   ├── statistical_summary.csv
│   ├── hotel_type_counts.csv
│   ├── cancellation_counts.csv
│   ├── monthly_booking_counts.csv
│   ├── hotel_wise_cancellation.csv
│   ├── market_segment_counts.csv
│   ├── bangkok_data_quality.csv
│   ├── bangkok_statistical_summary.csv
│   ├── bangkok_room_types.csv
│   ├── bangkok_top_neighbourhoods.csv
│   └── PNG chart files
│
├── hospitality_analysis.py
├── bangkok_analysis.py
├── README.md
└── requirements.txt
```

## Installation

Clone the repository:

```bash
git clone https://github.com/tamkhanejanhvi123-afk/Hospitality-Data-Analysis.git
```

Move into the project folder:

```bash
cd Hospitality-Data-Analysis
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Make sure both CSV datasets are placed inside the `data` folder before running the scripts.

## Run the Project

To analyse hotel booking data:

```bash
python hospitality_analysis.py
```

To analyse Bangkok accommodation listings:

```bash
python bangkok_analysis.py
```

The analysis results, CSV reports, and charts are saved in the `outputs` folder.

## Conclusion

This project helped me understand how Python can be used to analyse hospitality data. Through these two datasets, I explored hotel booking cancellations, customer booking patterns, accommodation types, listing prices, and neighbourhood distribution.

I also gained practical experience in data collection, data cleaning, handling missing values, checking duplicates, descriptive statistics, and data visualisation.

The project improved my understanding of how data analysis can help identify patterns and support better decision-making in the hospitality industry.

## Important Note

The Hotel Booking Demand dataset contains historical booking records, while the Inside Airbnb dataset contains accommodation listings. They represent different types of hospitality data and should not be treated as directly comparable. The findings describe the datasets analysed and do not represent live market conditions.
