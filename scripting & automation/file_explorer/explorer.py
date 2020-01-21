# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 13:42:08 2020

@author: simiyu
"""


"""
This Script will be able to move or delete files and folders
Use forward slash in windows file path and back slsh in linux
"""

# importing os module  
import os  
  
# importing shutil module  
import shutil, glob


#Move file and Create destination folder if it does not exist
def moveAndCreateDir(sourcePath, dstDir):
    # Check if dst path exists
    if os.path.isdir(dstDir) == False:
        # Create all the dierctories in the given path
        os.makedirs(dstDir); 
    # Move the file to path    
    return shutil.move(sourcePath, dstDir);
    
    
#Move all files in a directory to an another directory recursively
def moveAllFilesinDir(srcDir, dstDir):
    # Check if both the are directories
    if os.path.isdir(srcDir):
        if os.path.isdir(dstDir) == False:
            # Create all the dierctories in the given path
            os.makedirs(dstDir);
        # Iterate over all the files in source directory
        for filePath in glob.glob(srcDir + '\*'):
            # Move each file to destination Directory
            shutil.move(filePath, dstDir);
        return dstDir
    else:
        print("srcDir & dstDir should be Directories")
        
    
    
def main():
    print("**** Follow the prompts carefully to move or delete files and folders ****") 
    
    choice = str(input("Enter 'M' for moving and 'D' for deletion  : "))
    
    if(choice == 'M'):
        # Enter Source 
        source = str(input("Enter Absolute/Relative path of source file/folder : "))
        print("Source File/Folder Exists", os.path.exists(source))
        # Enter Destination
        dest = str(input("Enter Absolute/Relative path of destination folder : "))
        
        
        if os.path.exists(source) and os.path.isdir(source):
            print("Folder Copied to :", moveAllFilesinDir(source, dest))
        if os.path.exists(source) and os.path.isfile(source):
            print("File Copied to :", moveAndCreateDir(source, dest))
            
    if(choice == 'D'):
        # Enter Source 
        file = str(input("Enter Absolute/Relative path of file/folder : "))
        if os.path.exists(file) and os.path.isdir(file):
            print("Folder Deleted :", shutil.rmtree(file))
        if os.path.exists(file) and os.path.isfile(file):
            print("File Deleted :", os.remove(file))
        
        
    if(choice != 'M' and choice != 'D'):
        main()
        
    

if __name__ == '__main__':
    main()
    