#https://github.com/MrValdez/pycon-apac-2023

import PySimpleGUI as sg
import random
import time

timeout = 3

with open("cafe_menu.txt") as f:
  menu = f.readlines()

random.shuffle(menu)

name = menu[0].strip()
layout = [
    [sg.Image(f"{name}.png", key="image")],                     # png, gif
    [sg.Text(name, key="text", justification="center")],
]

window = sg.Window("PyCon APAC 2023", layout)

for name in menu[1:]:
    event, values = window.read(timeout=timeout * 1000)
    if event == sg.WIN_CLOSED:
        break

    name = name.strip()
    window["image"].update(filename=f"{name}.png")
    window["text"].update(name)
    window["text"].expand(True, True, True)

    window.move_to_center()
    window.refresh()

time.sleep(timeout)
window.close()

for name in menu:
    print(name.strip())