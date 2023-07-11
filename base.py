import tabula

# Set the path to your PDF file
pdf_path = "test.pdf"

# Convert the PDF to an Excel file
tabula.convert_into(pdf_path, "output.xlsx", output_format="xlsx", pages="all")
