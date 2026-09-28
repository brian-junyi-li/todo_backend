from fastapi import FastAPI
from app.database import supabase
from app.router import users, task
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
    


app.include_router(users.router, prefix = "")
app.include_router(task.router, prefix = "")
