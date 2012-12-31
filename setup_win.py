import sys
from cx_Freeze import setup, Executable


base = None
if sys.platform == 'win32':
        base = "Win32GUI"
        
executables = [
        Executable("main.py", icon="img/icon.ico",
                   appendScriptToExe=True, appendScriptToLibrary=False,
                   base = base)
]

buildOptions = dict(
        create_shared_zip = False)


setup(  name = "Bombersquare",
        version = "1.0",
        description = "Bomberman clone with squares",
        options = dict(build_exe = buildOptions),
        executables = executables)
