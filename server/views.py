from fastapi import Request

from . import *


@app.get('/')
async def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})
