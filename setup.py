import os
import cx_Freeze

os.environ['TCL_LIBRARY'] = r'C:\\Users\\adamh\\AppData\\Local\\Programs\\Python\\Python36\\tcl\\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\\Users\adamh\\AppData\\Local\\Programs\\Python\\Python36\\tcl\\tk8.6'
executables = [cx_Freeze.Executable("start.py", base="Win32GUI")]
cx_Freeze.setup(
    name="Bubble Sorting Visualization",
    options={"build_exe": {
        "include_files": ["logo.png", "finsound.wav", "config.txt"]}},
    version="1.0",
    description="Bubble Sorting Interactive Visualizer",
    executables=executables)
