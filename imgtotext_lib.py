# Text to String
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

# Image prossecing
from PIL import Image
import os, platform

def clear():
    if platform.system().lower() == 'windows':
        os.system('cls')
    else:
        os.system('clear')

def convert_image(image_path: str, text_path: str, lang: str = 'eng'):
    # Open image
    img = Image.open(image_path)
    
    # Print image information (not necessary)
    # print(img)

    result = pytesseract.image_to_string(img, lang=lang, config='bazaar')

    with open(text_path, 'w') as file:
        file.write(result)
    
    return result
