#!/usr/bin/env python3

from fastapi import FastAPI
from app.routers import users
import uvicorn

app = FastAPI()

app.include_router(users.router)


@app.get('/')
async def root():
    return {'message': 'This is just an MVP'}


if __name__ == '__main__':
    uvicorn.run(app=app, host='0.0.0.0', port=8080)
