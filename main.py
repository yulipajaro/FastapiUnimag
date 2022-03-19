from fastapi import FastAPI
from funtions import function_routes
from fastapi.responses import RedirectResponse


app=FastAPI()
@app.get('/')
def redirigir():
     return RedirectResponse('http://localhost:8000/docs') 

app.include_router(function_routes)