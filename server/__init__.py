import os

from dotenv import load_dotenv

from .views import *


load_dotenv()

SECRET_KEY = os.environ.get('SECRET_KEY')
