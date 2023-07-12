import pandas as pd
import os

# Get a list of all the CSV files in the current directory
csv_files = [f for f in os.listdir() if f.endswith('.csv')]

# Create a Pandas Excel writer using openpyxl as the engine
writer = pd.ExcelWriter('merged.xlsx', engine='openpyxl')

# Loop through the list of CSV files and read each one into a DataFrame
for file in csv_files:
    df = pd.read_csv(file)
    # Write each DataFrame to a separate sheet in the Excel file
    df.to_excel(writer, sheet_name=os.path.splitext(file)[0], index=False)

# Save the Excel file
writer._save()
