# write_file.py

import os
from google.genai import types


def write_file(working_directory, file_path, content):
    working_dir_path = os.path.abspath(working_directory)
    target_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not target_file_path.startswith(os.path.join(working_dir_path, "")):
        return f"Error: Cannot write to \"{file_path}\" as it is outside the permitted working directory"
    
    try:
        if not os.path.exists(target_file_path):
            os.makedirs(os.path.dirname(target_file_path), exist_ok=True)
        
        if os.path.exists(target_file_path) and os.path.isdir(target_file_path):
            return f"Error: \"{target_file_path}\" is a directory, not a file"
        
        with open(target_file_path, "w") as f:
            f.write(content)
            
        return f"Successfully wrote to \"{file_path}\" ({len(content)} characters written)"
    except Exception as e:
        return f"Error: {e}"
    

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write the given content to the file at the target file path, creating the file if it does not exist already, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The target file path for writing the content, relative to the working directory. Creates this file if it does not exist already.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to be written to the target file path."
            ),
        },
    ),
)