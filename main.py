from autograder import grade_code
from directoryparser import sort_directories

honors_path = "C:/Users/prest/hw1-honors-submissions"
normal_path = "C:/Users/prest/hw1-submissions"

honors, normal = sort_directories(honors_path), sort_directories(normal_path)
for directory in normal:
    path = "C:/Users/prest/hw1-submissions/hw1-" + directory
    grade_code(path, input_data = "8\n12\n")