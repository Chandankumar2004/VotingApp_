# config.py
import os
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-change-me")
SQLALCHEMY_DATABASE_URI = os.getenv(
    "DATABASE_URL",
    "sqlite:///c:/Users/chand/Downloads/VotingApp_Python/VotingApp_Python/instance/votes.db"
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
ADMIN_SECRET = os.getenv("ADMIN_SECRET", "let-me-in")
