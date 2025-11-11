import os

from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

from dotenv import load_dotenv


__all__ = ['app', 'templates']

load_dotenv()

SECRET_KEY = os.environ.get('SECRET_KEY')

app = FastAPI()

templates = Jinja2Templates(directory='templates')
