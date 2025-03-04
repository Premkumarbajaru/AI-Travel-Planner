import os
from dotenv import load_dotenv

def load_api_key():
    load_dotenv()
    return os.getenv('API_KEY')
