import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('VKTOKEN')
USER_ID = int(os.getenv('USER_ID'))