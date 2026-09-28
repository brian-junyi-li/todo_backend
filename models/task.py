from sqlalchemy import Column, Integer, String, ForeignKey

from sqlalchemy.orm import Base
from sqlalchemy import String, Integer, Column, Boolean

from sqlalchemy.orm import mapped_column, Mapped,

from datetime import datetime

from app.models.models import Base

from uuid import UUID
class task(Base)
    __tablename__ = "task"
    id: Mapped[UUID] = mapped_column(primary_key=True, index=True)
    task_title: Mapped[str] = mapped_column(String(100), nullable=False)
    task_description: Mapped[str] = mapped_column(String(255), nullable=True)
    deadline: Mapped[datetime] = mapped_column(nullable=True)
    status: Mapped[str] = mapped_column(String(50), nullable=False, default="pending")
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, onupdate=datetime.utcnow)