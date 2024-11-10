import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    GROQ_API_KEY = os.getenv('GROQ_API_KEY')
