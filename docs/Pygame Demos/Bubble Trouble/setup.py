'''
Created on Jun 12, 2014

@author: burchtm
'''

#Class for making the game into an executable.
from cx_Freeze import setup, Executable  # @UnresolvedImport

copyDependentFiles=True
silent = True
includes = ["pygame","sys"]
setup(name='Bubble Trouble',
     version = "1.0",
     options = {
       "build_exe" : {
           "includes": includes,
           },
       },
     executables=[Executable('Bubble Trouble.py')],)