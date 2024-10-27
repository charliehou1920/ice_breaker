import os
from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
    print("Hello Charlie")
    api_key = os.getenv("OPENAI_API")
    print(f"OPENAI_API: {api_key}")
