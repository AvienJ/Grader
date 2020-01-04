# NAME: Clear Module
# FILE: __init__.py(DIR: .\)

# DESCRIPTION: "A module that clear the screen"
# CREDITS: Avien Jones(GITHUB: AvienJ)
# MISC\NOTES:
#   .Works with all big operating systems
#   .All in one file
# ____________________
import os
import platform

def clear():
  os_name = platform.system()
  if os_name == "Windows":
    os.system("cls")
  else:
    os.system("clear")
