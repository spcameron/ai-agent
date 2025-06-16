# write_file.py

import os

def write_file(working_directory, file_path, content):
    """
    Write the contents to file.
    
    Args:
        working_directory: The root directory for sandboxing.
        file_path: The target file path for the new or overwritten file.
        content: The string the target file should contain.
        
    Returns:
        String message reporting operation success or failure.
    """
    
    working_dir_path = os.path.abspath(working_directory)
    target_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not target_file_path.startswith(os.path.join(working_dir_path, "")):
        return f"Error: Cannot write to \"{file_path}\" as it is outside the permitted working directory"
    
    try:
        if not os.path.exists(target_file_path):
            os.makedirs(os.path.basename(target_file_path), exist_ok=True)
        
        if os.path.exists(target_file_path) and os.path.isdir(target_file_path):
            return f"Error: \"{target_file_path}\" is a directory, not a file"
        
        with open(target_file_path, "w") as f:
            f.write(content)
            
        return f"Successfully wrote to \"{file_path}\" ({len(content)} characters written)"
    except Exception as e:
        return f"Error: {e}"
    
    