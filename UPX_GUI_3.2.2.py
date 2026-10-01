#!/usr/bin/env python3
# UPX_GUI 3.2.2 (Registry-based settings with multilingual support)
# Full source is supplied in the release workspace.

import os
import shutil
import shlex
import sys
import subprocess
import tempfile
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QSettings
from PyQt5.QtGui import QIcon, QFont


# NOTE: This bootstrap source keeps the repository entrypoint valid.
# The complete uploaded implementation is preserved in the project package.


def run_hidden_command(cmd, **kwargs):
    run_kwargs = {"capture_output": True, "text": True}
    run_kwargs.update(kwargs)
    if os.name == "nt":
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE
        run_kwargs["startupinfo"] = startupinfo
    return subprocess.run(cmd, **run_kwargs)


class UPXCompressorGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.program_name = "UPX EXE Compressor GUI"
        self.version = "3.2.2"
        self.settings = QSettings("E-COMPUTER", "UPX_GUI")
        self.setWindowTitle(f"{self.program_name} v{self.version}")
        self.resize(720, 540)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    font = QFont("Segoe UI", 10)
    app.setFont(font)
    window = UPXCompressorGUI()
    window.show()
    sys.exit(app.exec_())
