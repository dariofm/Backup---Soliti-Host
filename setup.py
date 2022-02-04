from cx_Freeze import setup, Executable
 
setup(name='nome-do-arquivo',
    version='1.0',
    description='descrição do programa',
    options={'build_exe': {'packages': ['os'],"includes": ["mega","shutil","sqlite3","configparser"]}},
    executables = [Executable(
                   script='FileZip.py',
                   base=None
                   )
                  ]
)
"""import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["os"], "includes": ["mega","shutil","sqlite3","configparser"]}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "FileZip",
    version = "0.1",
    description = "My GUI application!",
    options = {"build_exe": build_exe_options},
    executables = [Executable("FileZip.py", base=base)]
)"""