from dotenv import load_dotenv
import os

# Load environment variables from a .env file into the environment
load_dotenv()

# Fetch the Cloudflare credentials from the environment
CLOUDFLARE_API_TOKEN = os.getenv("CLOUDFLARE_API_TOKEN")
CLOUDFLARE_ACCOUNT_ID = os.getenv("CLOUDFLARE_ACCOUNT_ID")
