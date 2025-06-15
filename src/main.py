import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

if sys.argv[1]:
    user_prompt = sys.argv[1]
else:
    print("Error: No prompt provided")
    
verbose = False
if "--verbose" in sys.argv:
    verbose = True
    
messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

response = client.models.generate_content(
    model="gemini-2.0-flash-001", contents=messages,
)

metadata = response.usage_metadata
prompt_tokens = metadata.prompt_token_count
response_tokens = metadata.candidates_token_count

if verbose:
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {response_tokens}")
    print()
print(response.text)