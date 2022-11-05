import os
from dotenv import load_dotenv 

load_dotenv()  # Load all the content of .env in environment variables

class Config:
    DEBUG = True

    FEED_URL = os.environ.get("FEED_URL", "")
    TW_API_KEY = os.environ.get("TW_API_KEY", "")
    TW_API_SECRET = os.environ.get("TW_API_SECRET", "")