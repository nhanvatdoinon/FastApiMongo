import uvicorn
from fastapi import FastAPI
from app.controller.student import route

app = FastAPI()
app.include_router(route)

if __name__ == 'main':
    uvicorn.run('app/main:app',host='127.0.0.1',port=8000,reload=True,debug = False)