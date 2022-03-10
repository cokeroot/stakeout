import os
import shutil
dirToSort = "StoringFiles" # StoringFiles contains all the copied files from the victim machine
dirList = os.listdir(dirToSort) # lists all files in StoringFiles
other = "other" # files with no extension
for file in dirList:
    fileName, extension = os.path.splitext(file) # splits the filename and extension by cutting off after the filename
    extension = extension[1:] # Everything that comes after the period is the extension
        
    if os.path.exists( dirToSort + '/' + extension ): # checks to see if directory for extension already exists
        shutil.move( dirToSort + '/' + file, dirToSort + '/' + extension + '/' + file ) # if it does, move the file into the the appropriate extension folder
        
    else: # if the directory for extension doesn't exist
        os.makedirs( dirToSort + '/' + extension ) # create the extension directory first
        shutil.move( dirToSort + '/' + file, dirToSort + '/' + extension + '/' + file ) # Then move the file into it's appropriate extension folder.

    if extension == "": # checks to see if filename doesn't have an extension
        #continue
        if os.path.exists( dirToSort + '/' + other ): # checks to see if directory for "other" already exists
            shutil.move( dirToSort + '/' + file, dirToSort + '/' + other + '/' + file ) # if it does, move the file into the the appropriate extension folder
        else:
            os.makedirs( dirToSort + '/' + other)
            shutil.move( dirToSort + '/' + file, dirToSort + '/' + other + '/' + file ) # if it does, move the file into the the appropriate extension folder