# Text to String
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

# Image prossecing
from PIL import Image
import os


def convert_image(image_path: str, text_path: str = 'foobar.txt', lang: str = 'eng'):
    img = Image.open(image_path)

    result = pytesseract.image_to_string(img, lang=lang, config='bazaar')

    with open(text_path, 'w') as file:
        file.write(result)
    
    return result

def convert_dir(dir_path: str, text_path: str = 'foobar.txt', lang: str = 'eng'):
    from rich.console import Console
    console = Console()
    for i, file in enumerate(os.scandir(dir_path)):
        file = str(file).replace("<DirEntry '", '')
        file = str(file).replace("'>", '')
        console.print(f'Reading File {file}', style='bold cyan')
        convert_image(f'{dir_path}/{file}', f'{dir_path}/{text_path}{i}.txt', lang=lang)
