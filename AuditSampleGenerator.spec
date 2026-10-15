# -*- mode: python ; coding: utf-8 -*-
# Build the GUI as a one-dir app (no %TEMP% unpack -> fewer AV ML detections).
# Usage:  pyinstaller --noconfirm --clean AuditSampleGenerator.spec
from PyInstaller.utils.hooks import collect_all

datas, binaries, hiddenimports = [], [], []
ret = collect_all('customtkinter')
datas += ret[0]
binaries += ret[1]
hiddenimports += ret[2]

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='AuditSampleGenerator',
    debug=False,
    strip=False,
    upx=False,
    console=False,
)

coll = COLLECT(
    a.binaries,
    a.datas,
    strip=False,
    upx=False,
    name='AuditSampleGenerator',
)
