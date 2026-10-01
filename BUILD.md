# Build Guide

## Windows

Install Python 3.10+ and dependencies:

```powershell
py -m pip install -r requirements.txt
py -m pip install pyinstaller
```

Build a standalone executable:

```powershell
pyinstaller --noconfirm --clean --windowed --onefile --name UPX-Compressor-GUI UPX_GUI_3.2.2.py
```

The resulting executable is placed in `dist/`.
