# in cmd run: python setup.py build
# make exe cu CX_FREEZE

"""
import sys
from cx_Freeze import setup, Executable
#  in cmd run: python setup.py build

setup(
    name="Ablieferung",
    version="2.1.0",
    description="Ablieferung maker.",
    executables=[Executable("setup.py", base="Win32GUI")])
"""

import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="Ablieferung",
        version="2.1.0",
        description="My GUI application!",
        options={"build_exe": build_exe_options},
        executables=[Executable("ablieferung_GUI.pyw", base=base)])
