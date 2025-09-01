# PDF OCR Alumni Records Extractor 📄

A Python script that extracts alumni names and registration numbers from scanned PDF documents using OCR (Optical Character Recognition) technology.

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Features](#features)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Description

This project automates the extraction of student/alumni information from scanned PDF documents. It converts PDF pages to images, crops specific regions containing names and registration numbers, preprocesses the images for better OCR accuracy, and extracts text data using Tesseract OCR.

**Problem it solves**: Manually typing alumni records from scanned PDFs is time-consuming and error-prone. This tool automates the process, saving hours of manual data entry work.

## Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd pdf-ocr-alumni-extractor
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Python dependencies**
```bash
pip install pytesseract pdf2image pillow opencv-python numpy
```

4. **Install system dependencies**

   **On Ubuntu/Debian:**
   ```bash
   sudo apt update
   sudo apt install tesseract-ocr poppler-utils
   ```

   **On macOS:**
   ```bash
   brew install tesseract poppler
   ```

   **On Windows:**
   - Download and install [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki)
   - Download and install [Poppler](http://blog.alivate.com.au/poppler-windows/)
   - Uncomment and update the tesseract path in the script

## Usage

1. **Place your PDF file** in the project directory
```bash
# Make sure your PDF is named 'alumni_records_removed.pdf'
# Or update the pdf_path variable in the script
```

2. **Configure cropping regions** (Important!)
```bash
# Run the script once to see cropped regions
python extract_alumni.py
```

3. **Adjust coordinates** in the script based on visual inspection
```python
NAME_BOX = (150, 110, 650, 160)     # Update these coordinates
REG_NO_BOX = (430, 470, 690, 510)   # Update these coordinates
```

4. **Run the extraction**
```bash
python extract_alumni.py
```

## Examples

### Sample Output
```
📄 Extracted Records:
------------------------------------------------------------
🔍 Showing cropped regions for tuning...

Record 1:
  Name       : JOHN SMITH
  Reg Number : REG001234
------------------------------------------------------------
Record 2:
  Name       : JANE DOE
  Reg Number : REG005678
------------------------------------------------------------
Record 3:
  Name       : ❌ Not found
  Reg Number : REG009012
------------------------------------------------------------
```

### Coordinate Configuration
```python
# Example coordinates for different PDF layouts
NAME_BOX = (150, 110, 650, 160)      # (x1, y1, x2, y2) for name region
REG_NO_BOX = (430, 470, 690, 510)    # (x1, y1, x2, y2) for reg number region
```

## Features

- **📑 PDF to Image Conversion** - High-quality 300 DPI conversion
- **✂️ Smart Cropping** - Precise region extraction for names and registration numbers
- **🖼️ Image Preprocessing** - Grayscale conversion and thresholding for better OCR
- **🔍 OCR Engine** - Tesseract OCR with optimized configuration
- **🎯 Targeted Extraction** - Focuses on specific data fields
- **🔧 Configurable Regions** - Easy coordinate adjustment for different PDF layouts
- **📊 Visual Debugging** - Shows cropped regions for manual verification
- **🧹 Text Cleaning** - Automatic text cleaning and formatting

## Configuration

### Adjusting Crop Regions

1. **Run the script once** to see the cropped regions displayed
2. **Manually inspect** the cropped areas shown
3. **Update coordinates** in the script:
   ```python
   NAME_BOX = (x1, y1, x2, y2)      # Left, Top, Right, Bottom
   REG_NO_BOX = (x1, y1, x2, y2)    # Left, Top, Right, Bottom
   ```

### OCR Configuration
```python
custom_config = r'--oem 3 --psm 6'  # OCR Engine Mode 3, Page Segmentation Mode 6
```

### Windows Tesseract Setup
```python
# Uncomment and update path on Windows
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

### PDF Settings
```python
dpi=300  # Higher DPI = better quality but slower processing
```

## Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/ocr-improvement
   ```
3. **Make your changes**
4. **Test with different PDF formats**
5. **Submit a pull request**

### Guidelines
- Test with various PDF layouts
- Follow PEP 8 for Python code
- Add comments for coordinate calculations
- Include sample PDFs in tests (if possible)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- **Tesseract OCR** - Google's open-source OCR engine
- **pdf2image** - PDF to image conversion library
- **OpenCV** - Image processing and computer vision
- **PIL/Pillow** - Python Imaging Library
- **NumPy** - Numerical computing library

---

**⚠️ Privacy Note**: Ensure you have proper authorization before processing any documents containing personal information. This tool is designed for legitimate data extraction purposes only.
