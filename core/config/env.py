import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Determine environment (default: local)
ENV = os.getenv("ENV", "local")

# Load base .env
load_dotenv(BASE_DIR / ".env")

# Optionally override with local or production
if ENV == "local":
    load_dotenv(BASE_DIR / ".env.local", override=True)
elif ENV == "development":
    load_dotenv(BASE_DIR / ".env.production", override=True)
elif ENV == "production":
    load_dotenv(BASE_DIR / ".env.production", override=True)
