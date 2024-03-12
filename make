# PyInstaller makefile

SCRIPT_NAME = your_script.py
ICON_FILE = icon.ico

PYINSTALLER_FLAGS = --onefile --windowed --icon=$(ICON_FILE)

build:
    @pyinstaller $(PYINSTALLER_FLAGS) $(SCRIPT_NAME)


.PHONY: build