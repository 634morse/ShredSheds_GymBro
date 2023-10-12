import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["tkinter", "ttkwidgets"],
    "includes": ["modules.gui", "modules.db_handler", "data.exercises"],
}

# base="Win32GUI" should be used only for Windows GUI app
base = "Win32GUI" if sys.platform == "win32" else None

setup(
    name="GymBro",
    version="0.1",
    description="WeightLifting PR App",
    options={"build_exe": build_exe_options},
    executables=[Executable("gymbro.py", base=base, icon="data/images/logo.ico")],
)