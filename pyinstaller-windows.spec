# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['simple_dhcp_server\\qt.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('simple_dhcp_server\\icon.ico', '.'),
        ('simple_dhcp_server\\icon.png', '.'),
        ('simple_dhcp_server\\simple-dhcp-server-qt.yml', '.'),
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
    name='Simple DHCP Server',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon="simple_dhcp_server\\icon.ico"
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='simple-dhcp-server-windows',
)
