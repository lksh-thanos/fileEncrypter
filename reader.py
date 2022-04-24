import os
import glob
import pyautogui
from getpass import getpass
import time

filepath = input("Give the file path...")
file_dir = "/".join(filepath.split(r"/")[:-1])

password = getpass("Password : ")

pyautogui.hotkey("ctrl", "alt" , "t")

time.sleep(2)

pyautogui.write(f" cd {file_dir}")

pyautogui.hotkey("enter")

time.sleep(1)

pyautogui.write(f"vim {filepath}")

pyautogui.hotkey("enter")

pyautogui.write(f"{password}")

time.sleep(1)

pyautogui.hotkey("enter")

time.sleep(1)

pyautogui.hotkey("enter")

time.sleep(1)

pyautogui.hotkey("alt" , "f10")