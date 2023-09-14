from fastapi import APIRouter

properties = APIRouter(prefix='/properties')

@properties.post('/')
def create_analitics_property():
    return {"message": "Hello World"}

@properties.get('/')
def get_analitics_property():
    return {"message": "Hello World"}

@properties.get('/me')
def get_me_analitics_property():
    return {"message": "Hello World"}
