from fastapi import APIRouter
router = APIRouter()

@router.get("/users")
async def read_users():
    return {"api_response": "sent successfully"}

@router.post("/users")
async def create_user(user: dict):
    supabase.table("users").insert({"name": user["name"], "email": user["email"], "password": user["password"]}).execute()
    return {"status": "success", "message": "User created successfully"}












    