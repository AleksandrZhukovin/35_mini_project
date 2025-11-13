from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.templating import Jinja2Templates

from .models import UserSignUp, User
from .db import Session, get_db


__all__ = ['app', 'index', ]

app = FastAPI()

templates = Jinja2Templates(directory='templates')


@app.get('/')
async def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.get('/sign-up')
async def sign_up(request: Request):
    return templates.TemplateResponse('sign_up.html', {'request': request})


@app.post('/sign-up')
async def sign_up(user: UserSignUp, db: Session = Depends(get_db)):
    if db.query(User).filter(username=user.username).first():
        raise HTTPException(400, 'User already exists')

    user = User(**user.dict())
    user.hash_password()
    db.add(user)
    db.commit()
    db.refresh(user)


@app.get('/log-in')
async def log_in(request: Request):
    return templates.TemplateResponse('login.html', {'request': request})