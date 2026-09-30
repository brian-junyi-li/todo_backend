from fastapi import APIRouter
router = APIRouter()
from app.database import supabase
from app.jwt import generate_jwt


@router.get("/users")
async def read_users():
    return {"api_response": "sent successfully"}

@router.post("/users")
async def create_user(user: dict):
    supabase.table("users").insert({"name": user["name"], "email": user["email"], "password": user["password"]}).execute()
    return {"status": "success", "message": "User created successfully"}


@router.post("/signup")
async def signup(user: dict):
    # Check if the user already exists
    existing_user = supabase.table("users").select("*").eq("email", user["email"]).execute().data
    if existing_user:
        return {"status": "error", "message": "User already exists"}

    # Create a new user
    supabase.table("users").insert({"name": user["name"], "email": user["email"], "password": user["password"]}).execute()
    jwt_token = generate_jwt({"email": user["email"], "name": user["name"]})
    return {"status": "success", "message": "User signed up successfully", "token": jwt_token}

@router.post("/login")
async def login(user: dict):
    # Check if the user exists
    existing_user = supabase.table("users").select("*").eq("email", user["email"]).execute().data
    print(existing_user)
    if not existing_user:
        return {"status": "error", "message": "Invalid credentials"}
    if existing_user[0]["password"] != user["password"]:
        return {"status": "error", "message": "Invalid credentials"}
    else:
        jwt_token = generate_jwt({"email": existing_user[0]["email"], "name": existing_user[0]["name"]})
        return {"status": "success", "message": "User logged in successfully", "token": jwt_token}
        




    