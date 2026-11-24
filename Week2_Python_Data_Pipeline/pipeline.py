import pandas as pd
import os
import logging
# Create output folder
os.makedirs("output", exist_ok=True)
# Configure logging
logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
def process_dataset(file_path, output_name):
    try:
        # 1. Data Ingestion
        logging.info(f"Loading {file_path}")
        df = pd.read_csv(file_path)
        print(f"Processing: {file_path}")
        print("Original shape:", df.shape)
        # 2. Data Inspection
        print("Missing values:", df.isnull().sum().sum())
        print("Duplicate rows:", df.duplicated().sum())
        # 3. Data Cleaning
        df = df.drop_duplicates()
        # 4. Data Transformation
        df.columns = df.columns.str.strip()
        # 5. Data Validation
        print("Cleaned shape:", df.shape)
        # 6. Data Storage
        output_path = f"output/{output_name}_cleaned.csv"
        df.to_csv(output_path, index=False)
        logging.info(f"Saved cleaned dataset: {output_path}")
        print("Saved successfully:", output_path)
    except Exception as e:
        logging.error(f"Error processing {file_path}: {e}")
        print("Error:", e)
# Run pipeline
if __name__ == "__main__":
    process_dataset(
        "data/hotel_bookings.csv",
        "hotel_bookings"
    )
    process_dataset(
        "data/bangkok_listings.csv",
        "bangkok_listings"
    )
    print("Data pipeline execution completed.")
