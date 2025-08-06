import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MODEL_PATH = os.getenv("MODEL_PATH")
    DATA_PATH = os.getenv("DATA_PATH")
    LOG_LEVEL = os.getenv("LOG_LEVEL")
    MODEL_VERSION = os.getenv("MODEL_VERSION")
    HOST = os.getenv("HOST")
    PORT = int(os.getenv("PORT"))