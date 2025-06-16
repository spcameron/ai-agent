# run_python.py

import os, subprocess
from google.genai import types


def run_python_file(working_directory, file_path):
    working_dir_path = os.path.abspath(working_directory)
    target_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not target_file_path.startswith(os.path.join(working_dir_path, "")):
        return f"Error: Cannot execute \"{file_path}\" as it is outside the permitted working directory"

    if not os.path.exists(target_file_path):
        return f"Error: File \"{file_path}\" not found"

    if not target_file_path[-3:] == ".py":
        return f"Error: \"{file_path}\" is not a Python file"

    try:
        result = subprocess.run(
            ["python3", target_file_path],
            timeout=30,
            capture_output=True,
            cwd= working_dir_path,
            text=True,
            )
        
        output_message = []
        
        if not result.stdout.strip() and not result.stderr.strip():
            output_message.append("No output produced")
        else:
            output_message.append(f"STDOUT: {result.stdout}")
            output_message.append(f"STDERR: {result.stderr}")
            
        if result.returncode != 0:
            output_message.append(f"Process exited with code {result.returncode}")
            
        return "\n".join(output_message)
    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute the Python file at the given file path, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path of the target Python file, relative to the working directory.",
            ),
        },
    ),
)