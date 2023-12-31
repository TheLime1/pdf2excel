import tabula
import os

def export_tables_to_csv(pdf_path, template_path):
    # Read the PDF using the template
    dfs = tabula.read_pdf_with_template(pdf_path, template_path)

    # Check if multiple tables were returned
    if isinstance(dfs, list):
        # Loop over each table
        for i, df in enumerate(dfs):
            # Convert the table to a CSV file with a unique filename
            csv_filename = f"output_{i}.csv"
            df.to_csv(csv_filename, index=False)
    else:
        # Only one table was returned
        df = dfs

        # Convert the table to a CSV file
        df.to_csv("output.csv", index=False)


def remove_csv_files():
    # Get a list of all files in the current directory
    files = os.listdir()

    # Loop over each file
    for file in files:
        # Check if the file is a CSV file
        if file.endswith(".csv"):
            # Remove the CSV file
            os.remove(file)