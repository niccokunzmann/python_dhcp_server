# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['dhcp_server\\qt.py'],
    pathex=[],
    binaries=[],
    datas=[
        'dhcp_server\\icon.ico',
        'dhcp_server\\icon.png',
        'dhcp_server\\python-dhcp-server-qt.yml'
    ],
    hiddenimports=[
        'pyyaml'
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
    [],
    exclude_binaries=True,
    name='Python DHCP Server',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='python-dhcp-server-qt',
)
