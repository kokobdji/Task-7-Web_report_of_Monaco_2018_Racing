import os

from dotenv import load_dotenv

load_dotenv()
PATH_TO_FILES = os.getenv('PATH_TO_FILES')


class Config:
    DEBUG = True
