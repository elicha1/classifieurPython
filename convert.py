from distutils.core import setup
import py2exe

# Remove the build folder, a bit slower but ensures that build contains the latest
import shutil
shutil.rmtree("build", ignore_errors=True)

# my setup.py is based on one generated with gui2exe, so data_files is done a bit differently
data_files = []
includes = []
excludes = ['_gtkagg', '_tkagg', 'bsddb', 'curses', 'pywin.debugger',
            'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
            'Tkconstants', 'Tkinter', 'pydoc', 'doctest', 'test', 'sqlite3'
            ]
packages = ['pytz']
dll_excludes = ['libgdk-win32-2.0-0.dll', 'libgobject-2.0-0.dll', 'tcl84.dll',
                'tk84.dll']
icon_resources = []
bitmap_resources = []
other_resources = []

# add the mpl mpl-data folder and rc file
import matplotlib as mpl
data_files += mpl.get_py2exe_datafiles()

setup(
    windows=['embedding_in_wx2.py'],
                          # compressed and optimize reduce the size
    options = {"py2exe": {"compressed": 2, 
                          "optimize": 2,
                          "includes": includes,
                          "excludes": excludes,
                          "packages": packages,
                          "dll_excludes": dll_excludes,
                          # using 2 to reduce number of files in dist folder
                          # using 1 is not recommended as it often does not work
                          "bundle_files": 2,
                          "dist_dir": 'dist',
                          "xref": False,
                          "skip_archive": False,
                          "ascii": False,
                          "custom_boot_script": '',
                         }
              },

    # using zipfile to reduce number of files in dist
    zipfile = r'lib\library.zip',

    console=("test.py")
)