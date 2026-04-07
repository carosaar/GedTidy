# GedTidy.spec

import sys
import os
from pathlib import Path

# Basisverzeichnis des Projekts (dort, wo du PyInstaller aufrufst)
BASE_DIR = Path(os.getcwd())

# src in den Suchpfad aufnehmen, damit 'gedtidy' importierbar ist
SRC_DIR = BASE_DIR / "src"
sys.path.insert(0, str(SRC_DIR))

from gedtidy.version import APP_VERSION  # jetzt aus dem Paket

block_cipher = None

a = Analysis(
    [str(SRC_DIR / "gedtidy" / "main.py")],
    pathex=[str(BASE_DIR), str(SRC_DIR)],
    binaries=[],
    datas=[
        (str(SRC_DIR / "gedtidy" / "ui"), "gedtidy/ui"),
        (str(SRC_DIR / "gedtidy" / "models"), "gedtidy/models"),
        (str(BASE_DIR / "assets" / "gedtidy.ico"), "assets"),
    ],
    hiddenimports=[
        'json',
        'datetime',
        're',
        'os',
        'PySide6',
        'PySide6.QtWidgets',
        'PySide6.QtCore',
        'PySide6.QtGui',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='GedTidy',
    icon=str(BASE_DIR / "assets" / "gedtidy.ico"),
    debug=False,
    strip=False,
    upx=False,
    console=False,
    filevers=tuple(map(int, APP_VERSION.split("."))),
    prodvers=tuple(map(int, APP_VERSION.split("."))),
    company_name='(c) 2026 Dieter Eckstein',
    product_name='GedTidy',
    description='GedTidy – Genealogical Data Cleaner',
)