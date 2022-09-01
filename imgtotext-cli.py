# Better CLI functions
import keyboard
from rich.console import Console
from rich.table import Table
from imgtotext_lib import convert_image, convert_dir
from rich import traceback
from time import sleep
import os # , sys
traceback.install()

console = Console()
choice = 0

def print_dir():
    global choice
    global console

    console.clear()
    directory = Table()
    directory.add_column('Choose a directory or a file', justify='left')

    dirs = os.listdir()

    for i, dir in enumerate(dirs):
        if i == choice:
            directory.add_row(dir, style='cyan')
        else:
            directory.add_row(dir)
    console.print(directory)

print_dir()

while True:
    sleep(.07)
    if keyboard.read_key() in ['w','up']:
        choice -= 1
        if choice < 0:
            choice = len(os.listdir())-1
        print_dir()

    elif keyboard.read_key() in ['s','down']:
        choice += 1
        if choice > len(os.listdir()):
            choice = 0
        print_dir()
    elif keyboard.is_pressed('esc'):
        break
    elif keyboard.is_pressed('enter'):
        if ('.png' in os.listdir()[choice] or 
             '.jpg' in os.listdir()[choice] or
             '.jpeg' in os.listdir()[choice]):
            console.print(f'Reading File {os.listdir()[choice]}', style='bold cyan')
            convert_image(os.listdir()[choice], './abc.txt', 'osd+equ+por')
        else:
            convert_dir(os.listdir()[choice], './abc', 'osd+equ+por')
        break




