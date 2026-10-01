# UPX Compressor GUI

A Windows-focused PyQt5 GUI for compressing and decompressing executable files with UPX.

## Features

- Compress and decompress executable files with UPX
- Configurable compression level
- Optional LZMA compression
- Backup and overwrite controls
- UPX path detection and testing
- File analysis
- Recent-file history
- Theme and language support
- Windows Registry settings via QSettings

## Requirements

- Python 3.10+
- PyQt5
- UPX available on PATH or configured manually

## Run

```bash
pip install -r requirements.txt
python UPX_GUI_3.2.2.py
```

## Build with PyInstaller

```bash
pip install -r requirements.txt
pyinstaller --noconfirm --clean --windowed --onefile --name UPX-Compressor-GUI UPX_GUI_3.2.2.py
```

Place `upx_icon.ico` beside the script when using the icon.

## License

MIT License. See `LICENSE`.
