from dotenv import load_dotenv
import os



load_dotenv()

api_key = os.environ.get("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("inavlid credential")
else:
    pass
