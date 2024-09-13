import os
import subprocess

def detect_language(file):
    if file.endswith('.java'):
        return 'java'
    elif file.endswith('.cpp'):
        return 'cpp'
    elif file.endswith('.py'):
        return 'python'
    return None

def compile_and_run_java(file_path, input_data):
    try:
        # Compile Java file
        compile_result = subprocess.run(['javac', file_path], capture_output=True, text=True)
        if compile_result.returncode != 0:
            print(f"Compilation failed for {file_path}:\n{compile_result.stderr}")
            return "Compilation Error"
        
        # Run the Java class
        class_file = file_path.replace('.java', '')
        run_result = subprocess.run(['java', class_file], input=input_data, capture_output=True, text=True)
        if run_result.returncode != 0:
            print(f"Runtime error for {file_path}:\n{run_result.stderr}")
            return "Runtime Error"
        
        print(f"Output for {file_path}:\n{run_result.stdout}")
        return "Success"
    
    except Exception as e:
        print(f"Error running {file_path}: {e}")
        return "Error"

def compile_and_run_cpp(file_path, input_data):
    try:
        # Compile C++ file
        exe_file = file_path.replace('.cpp', '')
        compile_result = subprocess.run(['g++', file_path, '-o', exe_file], capture_output=True, text=True)
        if compile_result.returncode != 0:
            print(f"Compilation failed for {file_path}:\n{compile_result.stderr}")
            return "Compilation Error"
        
        # Run the executable
        run_result = subprocess.run([f"./{exe_file}"], input=input_data, capture_output=True, text=True)
        if run_result.returncode != 0:
            print(f"Runtime error for {file_path}:\n{run_result.stderr}")
            return "Runtime Error"
        
        print(f"Output for {file_path}:\n{run_result.stdout}")
        return "Success"
    
    except Exception as e:
        print(f"Error running {file_path}: {e}")
        return "Error"

def run_python(file_path, input_data):
    try:
        # Run Python file and pass input_data as a string
        run_result = subprocess.run(['python', file_path], input=input_data, capture_output=True, text=True)
        if run_result.returncode != 0:
            print(f"Runtime error for {file_path}:\n{run_result.stderr}")
            return "Runtime Error"
        
        print(f"Output for {file_path}:\n{run_result.stdout}")
        return "Success"
    
    except Exception as e:
        print(f"Error running {file_path}: {e}")
        return "Error"

def grade_code(directory, input_data):
    hw_files = ['hw1.py', 'hw1.java', 'hw1.cpp']
    
    for hw_file in hw_files:
        file_path = os.path.join(directory, hw_file)
        if not os.path.exists(file_path):
            print(f"{hw_file} not found in {directory}. Skipping...")
            continue
        
        language = detect_language(hw_file)
        if language == 'java':
            print(f"Grading Java file: {hw_file}")
            result = compile_and_run_java(file_path, input_data)
        elif language == 'cpp':
            print(f"Grading C++ file: {hw_file}")
            result = compile_and_run_cpp(file_path, input_data)
        elif language == 'python':
            print(f"Grading Python file: {hw_file}")
            result = run_python(file_path, input_data)
        
        print(f"Result for {hw_file}: {result}")
        print("-" * 40)
