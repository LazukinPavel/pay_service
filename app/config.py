import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'I42oLBH8UYadhZKA5pFb'
