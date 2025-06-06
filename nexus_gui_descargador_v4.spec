
# nexus_gui_descargador_v4.spec
block_cipher = None

a = Analysis(
    ['nexus_gui_descargador_v4.py'],
    pathex=['.'],
    binaries=[
        ('yt-dlp.exe', '.'),
        ('ffmpeg.exe', '.'),
        ('ffprobe.exe', '.')
    ],
    datas=[
        ('logo.png', '.'),
        ('README_instalador_v4.txt', '.')
    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='NexusDownloader_v4',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='NexusDownloader_v4'
)
