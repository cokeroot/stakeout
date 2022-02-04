import os

# List files in the Users directory
# To find out what the name of the device user is

path = "C://Users"
users_list = os.listdir(path) # Lists directories from specified path
path_of_users = [] # make a list to store the path of user
print(f"Files and directories inside {path}:")
for dir in users_list:
    full_dir_path = os.path.join(path, dir)
    path_of_users.append(full_dir_path)
    
for path in path_of_users:
    print(f"{path}")

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

#for path in interesting_dirs:
    #print(path)

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
for path in interesting_dirs:
    full_file_paths = get_filepaths(path) # path is the starting path that the function will walk through
    for filepath in full_file_paths:
        print(filepath)