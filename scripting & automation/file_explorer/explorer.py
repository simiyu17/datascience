# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 13:42:08 2020

@author: simiyu
"""


"""
This Script will be able to move or delete files and folders by file extension
Remember if your source is file and not a directory, no filtering will be performed
"""

# importing os module  
import os  
  
# importing shutil module  
import shutil, glob


#Move file and Create destination folder if it does not exist
def move_or_delete_one_file(sourcePath, action, dstDir=None):
    if dstDir is not None and os.path.isdir(dstDir) == False:
        # Create all the dierctories in the given path
        os.makedirs(dstDir);
    if action == "M":
        # Move each file to destination Directory
        shutil.move(sourcePath, dstDir);
        print("File Moved :", sourcePath)
    if action == "D":
        os.remove(sourcePath)
        print("File Deleted :", sourcePath)        
        
                   
        
        
        
#Move all files in a directory to an another directory recursively and Create destination folder if it does not exist
def move_or_delete_all_files_in_dir(action, srcDir, dstDir=None, filter_extension=None):
    # Check if both the are directories
    if os.path.isdir(srcDir):
        if dstDir is not None and os.path.isdir(dstDir) == False:
            # Create all the dierctories in the given path
            os.makedirs(dstDir);
        # Iterate over all the files in source directory
        for filePath in glob.glob(srcDir + '\*'):
            if (filter_extension is None or filePath.lower().endswith(filter_extension)):
                if action == "M":
                    # Move each file to destination Directory
                    shutil.move(filePath, dstDir);
                    print("File Moved :", filePath)
                if action == "D":
                    os.remove(filePath)
                    print("File Deleted :", filePath)
        
    else:
        print("srcDir & dstDir should be Directories")
        
    
    
def main():
    print("**** Follow the prompts carefully to move or delete files and folders ****") 
    
    choice = str(input("Enter 'M' for moving and 'D' for deletion  : "))
    
    if(choice != 'M' and choice != 'D'):
        main()
    
    
    
    # Enter Source 
    source = str(input("Enter Absolute/Relative path of source file/folder : "))
    if(os.path.exists(source) == False):
        print("Source File/Folder Does Not Exist", source)
        main()
    print("Source File/Folder", source)
    
    if(choice == 'M'):
        # Enter Destination
        dest = str(input("Enter Absolute/Relative path of destination folder : "))
        print("Destination File/Folder", dest)
        
        if os.path.exists(source) and os.path.isdir(source):
            # Enter Source 
            f_extension = str(input("Enter File extensions (Leave Blank For All) : "))
            print("Folder Copied to :", move_or_delete_all_files_in_dir(choice, source, dest, f_extension))
        if os.path.exists(source) and os.path.isfile(source):
            print("File Copied to :", move_or_delete_one_file(source, choice, dest))
            
    if(choice == 'D'):
        if os.path.exists(source) and os.path.isdir(source):
            # Enter Source 
            f_extension = str(input("Enter File extensions (Leave Blank For All) : "))
            print("Folder Copied to :", move_or_delete_all_files_in_dir(choice, source, None, f_extension))
        if os.path.exists(source) and os.path.isfile(source):
            print("File Copied to :", move_or_delete_one_file(source, choice))
        
        
if __name__ == '__main__':
    main()
    