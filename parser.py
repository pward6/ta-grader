import os

def sort_directories(path):

    items = os.listdir(path)
    
    # Filter out the directories
    directories = [item[4:] for item in items if os.path.isdir(os.path.join(path, item))]
    # Sort the directories alphabetically    
    return directories

def find_median(dirs):
    return dirs[len(dirs) // 2 - 1]

path = "C:/Users/prest/hw1-submissions"
directories = sort_directories(path)
print(find_median(directories))