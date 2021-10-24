# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['Medidor_de_lag.py'],
             pathex=['C:\\Users\\raton\\source\\repos\\Medidor de lag\\Medidor de lag'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
a.datas += [("./Google.png", "Google.png", "DATA")]
a.datas += [("./Discord.png", "Discord.png", "DATA")]
a.datas += [("./lol.png", "lol.png", "DATA")]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='Medidor_de_lag',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
