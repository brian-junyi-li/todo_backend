from typing import Literal, Optional
from uuid import UUID

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field, field_validator

from app.database import supabase

router = APIRouter()

Status = Literal["pending", "in_progress", "completed"]


class TaskBase(BaseModel):
    title: str = Field(min_length=1)
    description: str = Field(min_length=1)
    status: Status
    user_id: UUID
    deadline: Optional[str] = None

    @field_validator("status", mode="before")
    @classmethod
    def lowercase_status(cls, v):
        return v.lower() if isinstance(v, str) else v

    @field_validator("deadline", mode="before")
    @classmethod
    def empty_deadline_to_none(cls, v):
        return v or None


class TaskCreate(TaskBase):
    pass


class TaskUpdate(TaskBase):
    id: UUID


class TaskDelete(BaseModel):
    id: UUID


def ensure_user_exists(user_id: UUID):
    if not supabase.table("users").select("id").eq("id", str(user_id)).execute().data:
        raise HTTPException(status_code=404, detail="Invalid user_id. User does not exist.")


def ensure_task_exists(task_id: UUID):
    if not supabase.table("task").select("id").eq("id", str(task_id)).execute().data:
        raise HTTPException(status_code=404, detail="Invalid task id. Task does not exist.")


@router.get("/task")
def get_task():
    return {"status": "success", "data": supabase.table("task").select("*").execute().data}


@router.post("/task", status_code=201)
def create_task(task: TaskCreate):
    ensure_user_exists(task.user_id)
    supabase.table("task").insert({
        "task_title": task.title,
        "task_description": task.description,
        "status": task.status,
        "user_id": str(task.user_id),
        "deadline": task.deadline,
    }).execute()
    return {"status": "success", "message": "Task created successfully"}


@router.patch("/task")
def update_task(task: TaskUpdate):
    ensure_user_exists(task.user_id)
    ensure_task_exists(task.id)

    changes = {
        "task_title": task.title,
        "task_description": task.description,
        "status": task.status,
    }
    # Only touch the deadline if the client sent one, so status-only updates don't wipe it
    if "deadline" in task.model_fields_set:
        changes["deadline"] = task.deadline

    supabase.table("task").update(changes).eq("id", str(task.id)).execute()
    return {"status": "success", "message": "Task updated successfully"}


@router.delete("/task")
def delete_task(task: TaskDelete):
    ensure_task_exists(task.id)
    supabase.table("task").delete().eq("id", str(task.id)).execute()
    return {"status": "success", "message": "Task deleted successfully"}
