# -*- mode: python ; coding: utf-8 -*-


from PyInstaller.utils.hooks import collect_all

selenium_datas, selenium_binaries, selenium_imports = collect_all('selenium')
manager_datas, manager_binaries, manager_imports = collect_all('webdriver_manager')

a = Analysis(
    ['menu_bot.py'],
    pathex=[],
    binaries=selenium_binaries + manager_binaries,
    datas=selenium_datas + manager_datas,
    hiddenimports=selenium_imports + manager_imports,
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
    name='menu_bot',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
