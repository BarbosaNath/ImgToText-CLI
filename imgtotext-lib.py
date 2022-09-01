# Text to String
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

# Image prossecing
from PIL import Image

def convert_image(image_path: str, text_path: str):
    # Open image
    img = Image.open(image_path)
    
    # Print image information (not necessary)
    print(img)

    result = pytesseract.image_to_string(img)

    with open(text_path, 'w') as file:
        file.write(result)
        print(result)
