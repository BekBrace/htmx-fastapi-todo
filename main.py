# FASTAPI Imports
from fastapi import FastAPI, Request, Header, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder

#Other Imports
from uuid import uuid4
from typing import Annotated, Union

# Initialize FastAPI
app = FastAPI()

#Configuring templates directory for Jinja2
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/todos", response_class=HTMLResponse)
async def list_todos(request: Request, hx_request: Annotated[Union[str, None], Header()] = None):
    if hx_request:
        return templates.TemplateResponse(
            request=request, name="todos.html", context={"todos":todos}
        )
    return JSONResponse(content=jsonable_encoder(todos)) 

@app.post("/todos", response_class=HTMLResponse)
async def create_todo(request: Request, todo: Annotated[str, Form()]):
    todos.append(TODO(todo))
    return templates.TemplateResponse(
        request=request, name="todos.html", context={"todos": todos}
    )

@app.put("/todos/{todo_id}", response_class=HTMLResponse)
async def update_todo(request: Request, todo_id: str, text: Annotated[str, Form()]):
    for index, todo in enumerate(todos):
        if str(todo.id) == todo_id:
            todo.text = text
            break
    return templates.TemplateResponse(
        request=request, name="todos.html", context={"todos": todos}
    )
    
@app.post("/todos/{todo_id}/toggle", response_class=HTMLResponse)
async def toggle_todo(request: Request, todo_id: str):
    for index, todo in enumerate(todos):
        if str(todo.id) == todo_id:
            todos[index].done = not todos[index].done
            break
    return templates.TemplateResponse(
        request=request, name="todos.html", context={"todos": todos}
    )

@app.post("/todos/{todo_id}/delete", response_class=HTMLResponse)
async def delete_todo(request: Request, todo_id: str):
    for index, todo in enumerate(todos):
        if str(todo.id) == todo_id:
            del todos[index]
            break
    return templates.TemplateResponse(
        request=request, name="todos.html", context={"todos": todos}
    )
# Todo Model
class TODO:
    def __init__(self, text:str):
        self.id = uuid4()
        self.text = text
        self.done = False

# In-memory storage for todos
todos = []
# Start the dev server (CLI use)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
    
    
    
# Sanity Test
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}