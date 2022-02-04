# As of right now, this file should be run instead of finduser.py this program imports finduser into itself.
from finduser import *
import shutil

cwd = os.getcwd() # Get the current working directory
storing_dir = "StoringFiles" # Directory created within current directory to store files
path_to_store = os.path.join(cwd, storing_dir) # Join path of current dir and storing dir to make full path
os.mkdir(storing_dir) # make directory to store copied files

print(f"path to store: {path_to_store}")

# Shows the DDD files of each User (These files don't exist for every user)
for path in interesting_dirs:
    full_file_paths = get_filepaths(path) # path is the starting path that the function will walk through
    for filepath in full_file_paths:
        try:
            shutil.copy(filepath, path_to_store)
        except OSError:
            pass
