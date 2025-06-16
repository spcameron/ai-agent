# get_files_info.py

import os
from google.genai import types


def get_files_info(working_directory, directory=None):
    working_dir_path = os.path.abspath(working_directory)
    target_dir_path = working_dir_path
    
    if directory:
        target_dir_path = os.path.abspath(os.path.join(working_directory, directory))
    
    # if target directory is not equal to or inside working_directory, return an error string
    if not (target_dir_path == working_dir_path or target_dir_path.startswith(os.path.join(working_dir_path, ""))):
        return(f"Error: Cannot list \"{directory}\" as it is outside the permitted working directory")
    
    # if target directory is not a directory, return an error string
    if not os.path.isdir(target_dir_path):
        return(f"Error: \"{directory}\" is not a directory")

    dir_contents = os.listdir(target_dir_path)
    
    str_contents = []
    for item in dir_contents:
        try:
            item_path = os.path.join(target_dir_path, item)
            file_name = os.path.basename(item_path)
            file_size = os.path.getsize(item_path)
            file_is_dir = os.path.isdir(item_path)
        except Exception as e:
            return f"Error: {e}"
            
        str_contents.append(f"- {file_name}: file_size={file_size} bytes, is_dir={file_is_dir}")
        
    return "\n".join(str_contents)


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)