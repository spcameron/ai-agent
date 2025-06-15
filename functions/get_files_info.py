# get_files_info.py

import os

def get_files_info(working_directory, directory=None):
    working_dir_path = os.path.abspath(working_directory)
    target_dir_path = os.path.abspath(directory)
    
    print(f"Working directory path: {working_dir_path}")
    print(f"Target directory path: {target_dir_path}")
    
    # if directory is not inside working_directory, return an error string
    if not target_dir_path.startswith(working_dir_path):
        return(f"Error: Cannot list \"{directory}\" as it is outside the permitted working directory")
    
    # if directory argument is not a directory, return an error string
    if not os.path.isdir(directory):
        return(f"Error: \"{directory}\" is not a directory")

    dir_contents = os.listdir(directory)
    
    str_contents = ""
    for item in dir_contents:
        try:
            file_name = os.path.basename(item)
            file_size = os.path.getsize(item)
            file_is_dir = os.path.isdir(item)
        except Exception as e:
            print(f"Error encountered: {e}")
            
        str_contents += f"{file_name}: file_size={file_size} bytes, is_dir={file_is_dir}"
        
    return str_contents