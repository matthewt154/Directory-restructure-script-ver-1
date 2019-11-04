import os
import shutil
#function to add files from directory to specific directory
#if already exists then just repaces 
def addNewDir(oldPath, newPath):
    for files in os.scandir(oldPath):
        #test if it's a file first of all
        if files.is_file():
            print(files)
            #filePath = str(oldPath+"/"+files)
            shutil.copy(files, newPath)
src='C:/Users/tran/Desktop/Travail/Martine/Air Quality'
dst= 'C:/Users/tran/Desktop/Travail/Martine/TestPy'
addNewDir(src, dst)
       
