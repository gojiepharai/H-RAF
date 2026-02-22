import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get API key
API_KEY = os.getenv("NVD_API_KEY")

print("Loaded API Key:", API_KEY)
