# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['C:/Users/cleme/code/python/Splatnet-for-PC/main.py'],
    pathex=[],
    binaries=[],
    datas=[('C:/Users/cleme/code/python/Splatnet-for-PC/200px-S2_Stage_Ancho-V_Games.png', '.'), ('C:/Users/cleme/code/python/Splatnet-for-PC/200px-S2_Stage_Arowana_Mall.png', '.'), ('C:/Users/cleme/code/python/Splatnet-for-PC/200px-S2_Stage_Blackbelly_Skatepark.png', '.'), ('C:/Users/cleme/code/python/Splatnet-for-PC/200px-S2_Stage_Camp_Triggerfish.png', '.'), ('C:/Users/cleme/code/python/Splatnet-for-PC/200px-S2_Stage_Goby_Arena.png', '.'), ('C:/Users/cleme/code/python/Splatnet-for-PC/200px-S2_Stage_Humpback_Pump_Track.png', '.'), ('C:/Users/cleme/code/python/Splatnet-for-PC/200px-S2_Stage_Inkblot_Art_Academy.png', '.'), ('C:/Users/cleme/code/python/Splatnet-for-PC/200px-S2_Stage_Kelp_Dome.png', '.'), ('C:/Users/cleme/code/python/Splatnet-for-PC/200px-S2_Stage_MakoMart.png', '.'), ('C:/Users/cleme/code/python/Splatnet-for-PC/200px-S2_Stage_Manta_Maria.png', '.'), ('C:/Users/cleme/code/python/Splatnet-for-PC/200px-S2_Stage_Moray_Towers.png', '.'), ('C:/Users/cleme/code/python/Splatnet-for-PC/200px-S2_Stage_Musselforge_Fitness.png', '.'), ('C:/Users/cleme/code/python/Splatnet-for-PC/200px-S2_Stage_New_Albacore_Hotel.png', '.'), ('C:/Users/cleme/code/python/Splatnet-for-PC/200px-S2_Stage_Piranha_Pit.png', '.'), ('C:/Users/cleme/code/python/Splatnet-for-PC/200px-S2_Stage_Port_Mackerel.png', '.'), ('C:/Users/cleme/code/python/Splatnet-for-PC/200px-S2_Stage_Shellendorf_Institute.png', '.'), ('C:/Users/cleme/code/python/Splatnet-for-PC/200px-S2_Stage_Skipper_Pavilion.png', '.'), ('C:/Users/cleme/code/python/Splatnet-for-PC/200px-S2_Stage_Snapper_Canal.png', '.'), ('C:/Users/cleme/code/python/Splatnet-for-PC/200px-S2_Stage_Starfish_Mainstage.png', '.'), ('C:/Users/cleme/code/python/Splatnet-for-PC/200px-S2_Stage_Sturgeon_Shipyard.png', '.'), ('C:/Users/cleme/code/python/Splatnet-for-PC/200px-S2_Stage_The_Reef.png', '.'), ('C:/Users/cleme/code/python/Splatnet-for-PC/200px-S2_Stage_Wahoo_World.png', '.'), ('C:/Users/cleme/code/python/Splatnet-for-PC/200px-S2_Stage_Walleye_Warehouse.png', '.'), ('C:/Users/cleme/code/python/Splatnet-for-PC/dbs.py', '.'), ('C:/Users/cleme/code/python/Splatnet-for-PC/game.py', '.'), ('C:/Users/cleme/code/python/Splatnet-for-PC/iksm.py', '.'), ('C:/Users/cleme/code/python/Splatnet-for-PC/image_1.png', '.'), ('C:/Users/cleme/code/python/Splatnet-for-PC/image_2.png', '.'), ('C:/Users/cleme/code/python/Splatnet-for-PC/image_3.png', '.'), ('C:/Users/cleme/code/python/Splatnet-for-PC/image_4.png', '.'), ('C:/Users/cleme/code/python/Splatnet-for-PC/image_5.png', '.'), ('C:/Users/cleme/code/python/Splatnet-for-PC/image_6.png', '.'), ('C:/Users/cleme/code/python/Splatnet-for-PC/image_home.png', '.'), ('C:/Users/cleme/code/python/Splatnet-for-PC/image_results.png', '.'), ('C:/Users/cleme/code/python/Splatnet-for-PC/salmonrun.py', '.'), ('C:/Users/cleme/code/python/Splatnet-for-PC/splatnet2statink.py', '.'), ('C:/Users/cleme/code/python/Splatnet-for-PC/test_schedule.py', '.'), ('c:\\users\\cleme\\appdata\\local\\programs\\python\\python310\\lib\\site-packages/customtkinter', 'customtkinter')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main',
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
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)
