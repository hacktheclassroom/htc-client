"""build.py"""

import cx_Freeze
import platform

executables = [cx_Freeze.Executable("htc_client/main.py")]

plat = platform.system()

include_files = [
    'htc_client/font.ttf'
]

if plat == 'Windows':
    cx_Freeze.setup(
        name="Hack The Classroom",
        options={"build_exe": {"packages":["pygame"],
                            "include_files":include_files}},
        executables = executables
    )
elif plat == 'Linux':
    cx_Freeze.setup(
        name="Hack The Classroom",
        options={"build_exe": {"packages":["pygame"],
                            "include_files":include_files}},
        executables = executables
    )
elif plat == 'Darwin':
    cx_Freeze.setup(
        name="Hack The Classroom",
        options={"build_exe": {"packages":["pygame"],
                            "include_files":include_files}},
        executables = executables
    )
else:
    print('Error! Invalid platform: {}'.format(plat))
