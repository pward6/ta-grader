import os

def sort_directories(path):

    items = os.listdir(path)
    
    directories = [item[4:] for item in items if os.path.isdir(os.path.join(path, item))]


    return directories[:len(directories) // 2]

def find_median(dirs):
    return dirs[len(dirs) // 2 - 1]