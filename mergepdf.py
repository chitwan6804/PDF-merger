from pypdf import PdfWriter
import os

# Initialize PdfWriter
merger = PdfWriter()

files = sorted(
    [file for file in os.listdir("clusterfiles") if file.endswith(".pdf")],
    key=lambda x: int(os.path.splitext(x)[0])  # Extract numeric part for sorting
)

# Append each file to the merger
for pdf in files:
    print(f"Adding file: {pdf}")  # Print the name of the file being added
    with open(os.path.join("clusterfiles", pdf), 'rb') as file:
        merger.append(file)

# Write the merged PDF to a new file
merger.write("DCN_fullnotes1.pdf")
merger.close()

