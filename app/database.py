from supabase import create_client
from dotenv import load_dotenv

import os

load_dotenv()  # Load environment variables from .env file

print("SUPABASE_URL:", os.getenv("SUPABASE_URL"))

supabase = create_client(

    supabase_url=os.getenv("SUPABASE_URL"),

    supabase_key=os.getenv("SUPABASE_KEY")

)
