# Ordered PDF Merger

**Ordered PDF Merger** is a simple Python script that combines multiple PDF files into a single document. The script ensures that files are merged in ascending order based on their numerical filenames (e.g., `1.pdf`, `2.pdf`, `10.pdf`). It's especially useful for organizing and combining PDF files in a batch where the order is critical.

## Features
- Merges PDF files located in a specified folder.
- Automatically sorts files in ascending numerical order based on filenames.
- Outputs a single PDF file combining all input files.

## Requirements
- Python 3.7 or higher
- [PyPDF](https://pypdf.readthedocs.io/en/latest/) library for handling PDF operations

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/chitwan6804/PDF-merger.git
   cd ordered-pdf-merger
   ```
2. Install the required Python dependencies:
   ```bash
   pip install pypdf
   ```

## Usage
1. Place all your PDF files in a folder named `clusterfiles` within the project directory.
2. Ensure the filenames are numeric (e.g., `1.pdf`, `2.pdf`, `3.pdf`) or have numbers as prefixes.
3. Run the script:
   ```bash
   python mergepdf.py
   ```
4. The merged PDF will be saved as `notes1.pdf` in the project directory.

## Contributing
Contributions are welcome! If you have suggestions for improvements or additional features, feel free to create a pull request or open an issue.
