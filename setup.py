import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "KeyPy",
        version = "1.0",
        author="Jhudin Aragonez , Julian Malagon,Alex Rincon",
        description = "Software Para el manejo de las llaves en la Universidad de Cudinamarca",
        options = {"build_exe": build_exe_options},
        executables = [Executable("KeyPy.py", base=base,icon="keypy3.ico")])
