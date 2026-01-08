#I hope it helps you guys <3

import pyautogui
import keyboard
import json
import time
import os

# pip install keyboard
# pip install pyautogui

file_name = "combinations.json"

special_keys = "alt", "space", "backspace", "tab", "ctrl", "esc"

default = {
    "77": "t",
    "88": "y",
    "t7": "T",
    "y8": "Y",
    "esc"*2: "tab"
}

if not os.path.exists(file_name):
    with open(file_name, "w") as f:
        json.dump(default, f, indent=4)
    print(f"Modifique el archivo: {file_name}")
    print(f"Vaya a https://github.com/Brick-Briceno/Brick-Keyboard/blob/main/README.md: {file_name}"
          "\n para más información")
    input()
    quit()


with open(file_name, "r") as f:
    combinations = json.load(f)
pressed_keys = ""
start = time.time()
def on_key_press(event):
    global start, pressed_keys
    key_name = event.name
    end = time.time() - start
    pressed_keys += key_name
    start = time.time()
    if end > 5: pressed_keys = key_name
    for key in combinations:
        if key in pressed_keys:
            if combinations[key] in special_keys:
                pyautogui.press(combinations[key])
            else:
                for _ in range(len(key)):
                    pyautogui.press("backspace")
                pyautogui.write(combinations[key])
            pressed_keys = ""


keyboard.on_press(on_key_press)

print("Escuchando combinaciones de teclas...")
keyboard.wait()
