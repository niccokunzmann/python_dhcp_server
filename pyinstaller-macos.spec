# -*- mode: python ; coding: utf-8 -*-
# Credits: https://www.pythonguis.com/tutorials/packaging-pyqt5-applications-pyinstaller-macos-dmg/

block_cipher = None


a = Analysis(
    ['simple_dhcp_server/macos.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('simple_dhcp_server/icon.ico', 'simple_dhcp_server'),
        ('simple_dhcp_server/icon.icns', 'simple_dhcp_server'),
        ('simple_dhcp_server/icon.png', 'simple_dhcp_server'),
        ('simple_dhcp_server/simple-dhcp-server-tk.conf', 'simple_dhcp_server'),
    ],
    hiddenimports=[
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Simple DHCP Server',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None,
          icon="icon.icns",
)
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='simple-dhcp-server-macos',
)
app = BUNDLE(coll,
             name='Simple DHCP Server.app',
             icon="simple_dhcp_server/icon.icns",
             bundle_identifier="eu.quelltext.dhcp",
)