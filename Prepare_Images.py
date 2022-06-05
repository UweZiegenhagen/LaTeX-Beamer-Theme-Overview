# -*- coding: utf-8 -*-
"""
@author: Uwe Ziegenhagen
"""
import os
import glob


# All files and directories ending with .txt and that don't begin with a dot:
files = glob.glob('Presentation*.tex')

for file in files:
    print(file)    
    os.system(f'pdflatex -interaction=batchmode {file}')
    os.system(f'pdflatex -interaction=batchmode {file}')


files_to_delete = ['log', 'toc', 'aux', 'nav', 'snm', 'out']

for filetype in files_to_delete:

    filelist = glob.glob(f'*.{filetype}')
    for f in filelist:
        os.remove(f)
