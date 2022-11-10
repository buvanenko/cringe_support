import os
from dotenv import load_dotenv

from vkbottle.user import User

load_dotenv()

TOKEN = os.getenv('VKTOKEN')
USER_ID = int(os.getenv('USER_ID'))

user = User(TOKEN)