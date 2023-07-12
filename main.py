from pdf2csv import *
from csv2xl import *

# Set the path to your PDF file
pdf_path = "test.pdf"

# Set the path to your template file
template_path = "sbi_template.json"

export_tables_to_csv(pdf_path, template_path)
merge_csv_to_excel('.', 'output.xlsx')
remove_csv_files()
