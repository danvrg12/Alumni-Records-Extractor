import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import cv2
import numpy as np

# Optional: Set tesseract path if needed (Windows only)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Path to your scanned PDF
pdf_path = "alumni_records_removed.pdf"

# Step 1: Convert PDF to list of images (one per page)
pages = convert_from_path(pdf_path, dpi=300)

# Step 2: Define cropping regions — replace after manual inspection!
# Format: (x1, y1, x2, y2)
NAME_BOX = (150, 110, 650, 160)         # CHANGE ME after checking visually
REG_NO_BOX = (430, 470, 690, 510)       # CHANGE ME after checking visually

# OCR config
custom_config = r'--oem 3 --psm 6'

# Image preprocessing function
def preprocess_image(pil_img):
    img = np.array(pil_img)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    return Image.fromarray(thresh)

print("\n📄 Extracted Records:\n" + "-"*60)

for i, page in enumerate(pages):
    # Step 3: Crop name & reg number areas
    name_crop = page.crop(NAME_BOX)
    reg_crop = page.crop(REG_NO_BOX)

    # DEBUG: Show cropped areas for manual verification
    if i == 0:
        print("🔍 Showing cropped regions for tuning...")
        name_crop.show(title="Name Crop")
        reg_crop.show(title="Reg No. Crop")

    # Step 4: Preprocess both regions
    name_img = preprocess_image(name_crop)
    reg_img = preprocess_image(reg_crop)

    # Step 5: OCR on both preprocessed regions
    name_text = pytesseract.image_to_string(name_img, config=custom_config).strip()
    reg_text = pytesseract.image_to_string(reg_img, config=custom_config).strip()

    # Step 6: Clean and print results
    name = name_text.replace("\n", " ").strip()
    reg_no = reg_text.replace("\n", " ").strip()

    print(f"Record {i+1}:")
    print(f"  Name       : {name if name else '❌ Not found'}")
    print(f"  Reg Number : {reg_no if reg_no else '❌ Not found'}")
    print("-" * 60)
