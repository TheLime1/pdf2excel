import PySimpleGUI as sg
import os.path
import fitz
from io import BytesIO
from PIL import Image
from pdf2csv import *
from csv2xl import *

# First the window layout in 2 columns

file_list_column = [
    [
        sg.Text("PDF Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
        )
    ],
]

# For now will only show the name of the file that was chosen
pdf_viewer_column = [
    [sg.Text("Choose a PDF from list on left:")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Image(key="-IMAGE-", size=(400, 400))],
]

# Button for converting PDF to CSV and Excel
convert_button = sg.Button("Convert to CSV and Excel", key="-CONVERT-", disabled=True)

# ----- Full layout -----
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(pdf_viewer_column),
        sg.VSeperator(),
        convert_button,
    ]
]

window = sg.Window("PDF Viewer", layout, resizable=True)

# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    # Folder name was filled in, make a list of files in the folder
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            # Get list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith(".pdf")
        ]
        window["-FILE LIST-"].update(fnames)
    elif event == "-FILE LIST-":  # A file was chosen from the listbox
        try:
            filename = os.path.join(values["-FOLDER-"], values["-FILE LIST-"][0])
            window["-TOUT-"].update(filename)

            # Open PDF and convert first page to image
            with fitz.open(filename) as doc:
                page = doc.load_page(0)
                pix = page.get_pixmap()
                img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                with BytesIO() as b:
                    img.save(b, format="PNG")
                    window["-IMAGE-"].update(data=b.getvalue())
                    window["-CONVERT-"].update(disabled=False)

        except:
            pass
    elif event == "-CONVERT-":  # Convert PDF to CSV and Excel
        try:
            pdf_path = filename  # Path of the previewed PDF
            template_path = "C:/Users/everp/Documents/GitHub/pdf2excel/sbi_template.json"

            export_tables_to_csv(pdf_path, template_path)
            merge_csv_to_excel(".", "output.xlsx")
            remove_csv_files()

            sg.popup("Conversion completed successfully!")

        except Exception as e:
            sg.popup_error(f"An error occurred during conversion: {str(e)}")

window.close()
