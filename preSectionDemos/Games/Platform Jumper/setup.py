from cx_Freeze import setup, Executable  # @UnresolvedImport

copyDependentFiles=True
silent = True
includes = ["pygame","sys","time", "os"]
setup(name='Platform Jumper',
     version = "1.0",
     options = {
       "build_exe" : {
           "includes": includes,
           },
       },
     executables=[Executable('main.pyw', base = "Win32GUI")],)