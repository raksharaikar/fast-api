from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional


from pydantic import BaseModel

app = FastAPI()



  
  
todos = [
    
]


dashboard_data = [
    {
  "tasksCompleted": 10,
  "totalTasks": 19,
  "latestTasks": [
    {
      "id": "2",
        "item": "Cycle around town."
    }
  ]
}
]


token_data = [
    {
  "token": {
    "name": "jen",
    "token": "f94b01164ea17050a61e859b"
  },
  "image": "/images/profile.jpg"
}
]



class Item(BaseModel):
    id: int
    name: str
    completed: Optional[bool] = None

app = FastAPI()

origins = [
    "http://localhost:3001",
    "localhost:3001",
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
)


@app.post("/login", tags=["root"])
async def login_into_system() -> dict:
    return {"token": token_data}


@app.get("/todo", tags=["todos"])
async def get_todos() -> dict:
    return { "data": todos }

@app.get("/dashboard", tags=["todos"])
async def get_dashboard_data() -> dict:
    return { "data": dashboard_data }




@app.post("/todo", tags=["todos"])
async def add_todo(todo: dict) -> dict:
    todos.append(todo)
    return {
        "data": { "Todo added." }
    }


@app.put("/todo/{id}", tags=["todos"])
async def update_todo(id: int, body: dict) -> dict:
    for todo in todos:
        if int(todo["id"]) == id:
            todo["item"] = body["item"]
            return {
                "data": f"Todo with id {id} has been updated."
            }

    return {
        "data": f"Todo with id {id} not found."
    }


@app.delete("/todo/{id}", tags=["todos"])
async def delete_todo(id: int) -> dict:
    for todo in todos:
        if int(todo["id"]) == id:
            todos.remove(todo)
            return {
                "data": f"Todo with id {id} has been removed."
            }

    return {
        "data": f"Todo with id {id} not found."
    }
