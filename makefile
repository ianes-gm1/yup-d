# PyInstaller makefile

SCRIPT_NAME = "Yup_d - GUI.py"
ICON_FILE = icon.ico
DIRECTORY= ""
PYINSTALLER_FLAGS = --onefile --windowed --clean --console --icon=$(ICON_FILE) --distpath=$(DIRECTORY)
build:
	@pyinstaller $(PYINSTALLER_FLAGS) $(SCRIPT_NAME)
install_dependencies:
	pip install -r requirements.txt
.PHONY: install_dependencies build