'''
 #Program to restructure directories using os scripting
 #Subdirectories and main directories will be switch and files will change location 
 #Ex. main > sub > file will become:
 # sub > main > file 
 #application: if you made a mistake organising files and want to reorganise 
 #transfer to a new directory with different structure 
@author: Matthew Tran
'''
import os
from collections import defaultdict
import shutil
#function to add files from directory to specific directory
#if already exists then just replaces 
def addNewDir(oldPath, newPath):
    for files in os.scandir(oldPath):
        #test if it's a file first of all
        if files.is_file():
            print(files)
            shutil.copy(files, newPath)

def restructDir(rootdir, newRootDir):
    #function takes an initial root directory and a new root directory to copy to as parameters  
    #changes the directory structure as required and copies files at the end 

    #rootdir = 'C:/Users/tran/Desktop/Travail/Martine/Buildings'

    oldFolders=[] #list of folder paths 
    buildingnames=[]
    subf=defaultdict(list) #key is building folder, value is sub folder name
    subfpaths=defaultdict(list) #now containing paths of suboldFolders  
    for entry in os.scandir(rootdir): #get all the initial files (buildings)
        if entry.is_dir():
            oldFolders.append(entry.path)
            buildingnames.append(os.path.basename(entry.path)) #list containing all buildnames from parsing
            

    for folder in oldFolders: #parse through each folder for subdirect., then get files
        for entry in os.scandir(folder):
            if entry.is_dir():
                key=os.path.basename(folder) #key name is string of folder (building)
                subf[key].append(os.path.basename(entry.path).lower()) #adding name of subfolder
                #could add name of path to identify 
                subfpaths[key].append(entry.path)
                #for files in os.listdir(entry.path):
                    #print (files)
                    
    #print(subf)
    #string manipulation to make new directory path with subdir (issues) before building 
    newDirPaths=[] #list of new folder names for issues

    for keys in subf: #accessing dictionary of lists 
        for stuff in subf[keys]:
            #print(stuff)
            if stuff not in newDirPaths:
                newDirPaths.append(stuff)
                
    #print (newDirPaths)

    #newRootDir = 'C:/Users/tran/Desktop/Travail/Martine/TestPy/'

        
    for folders in newDirPaths:
        
        addDir = str(newRootDir+folders)
        #delete old directories in that file (FOR TESTING) can comment out
        shutil.rmtree(addDir)
        os.mkdir(addDir) #creating new directories 
    #take the files from the old directories and associate in new directories
    #print(subfpaths)
    for folders in oldFolders: #parse through subdirectory paths in old folders
        for entry in os.scandir(folders):
            if entry.is_dir():
                name= os.path.basename(entry.path).lower()
                if (name in newDirPaths): #if folders in old correspond to new created folders
                    '''
                    have to make new folder (organise so that old folder is now
                    subdirectory of new folder
                    '''
                    folderName= os.path.basename(folders) #extract just name of folder not path
                    newPath = str(newRootDir+ name+ "/"+folderName)
                    oldPath=str(folders+"/"+name.casefold()) #casfold (doesn't matter if capitalised or not 
                    #create directory with name of old(folders)
                    os.mkdir(newPath)          
                    addNewDir(oldPath, newPath ) #calling method to add files to keys
                    print("Success")

    return 0

rootdir = 'C:/Users/tran/Desktop/Travail/Martine/Buildings'
newRootDir = 'C:/Users/tran/Desktop/Travail/Martine/TestPy/'
restructDir(rootdir, newRootDir)

            

