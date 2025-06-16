# main.py

import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from prompts import system_prompt
from call_function import available_functions, call_function
from config import MAX_ITERATIONS


def main():
    load_dotenv()
    
    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    if not args:
        print("Error: No prompt provided")
        
    user_prompt = " ".join(args)
    
    if verbose:
        print(f"User prompt: {user_prompt}")
        
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    
    generate_content(client, messages, verbose)


def generate_content(client, messages, verbose):
    for _ in range(MAX_ITERATIONS):
        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions],
                system_instruction=system_prompt,
            ),
        )
        
        if response.candidates:
            for candidate in response.candidates:
                messages.append(candidate.content)

        metadata = response.usage_metadata
        prompt_tokens = metadata.prompt_token_count
        response_tokens = metadata.candidates_token_count        
        
        if verbose:
            print(f"Prompt tokens: {prompt_tokens}")
            print(f"Response tokens: {response_tokens}")

        if not response.function_calls:
            print(f"Final response: {response.text}")
            return
        
        for function_call_part in response.function_calls:
            function_call_result = call_function(function_call_part, verbose)
            messages.append(function_call_result)
            if not function_call_result.parts[0].function_response.response:
                raise Exception(f"Fatal error: The call to {function_call_part.name} returned no response")
            elif verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")


    

    

if __name__ == "__main__":
    main()