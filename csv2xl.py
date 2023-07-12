import pandas as pd
import os

def merge_csv_to_excel(directory, output_file):
    # Get a list of all the CSV files in the specified directory
    csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]

    # Create a Pandas Excel writer using openpyxl as the engine
    writer = pd.ExcelWriter(output_file, engine='openpyxl')

    # Loop through the list of CSV files and read each one into a DataFrame
    for file in csv_files:
        df = pd.read_csv(os.path.join(directory, file))
        # Write each DataFrame to a separate sheet in the Excel file
        df.to_excel(writer, sheet_name=os.path.splitext(file)[0], index=False)

    # Save the Excel file
    writer._save()
