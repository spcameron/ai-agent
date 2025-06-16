# get_file_content.py

import os
from google.genai import types

from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    working_dir_path = os.path.abspath(working_directory)
    target_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not target_file_path.startswith(os.path.join(working_dir_path, "")):
        return f"Error: Cannot read \"{file_path}\" as it is outside the permitted working directory"
    
    if not os.path.isfile(target_file_path):
        return f"Error: File not found or is not a regular file: \"{file_path}\""
    
    try:
        with open(target_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS + 1)
            if len(file_content_string) > MAX_CHARS:
                file_content_string = file_content_string[:MAX_CHARS] + f"\n[...File \"{file_path}\" truncated at 10000 characters]"
            else:
                file_content_string = file_content_string[:MAX_CHARS]
            return file_content_string
    except Exception as e:
        return f"Error: {e}"


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Lists contents in the specified file path up to a configured maximum character length, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to list the contents of, relative to the working directory.",
            ),
        },
    ),
)