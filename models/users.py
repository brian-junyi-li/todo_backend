from sqlalchemy import Column, Integer, String, ForeignKey

from sqlalchemy.orm import Base
from sqlalchemy import String, Integer, Column, Boolean

from sqlalchemy.orm import mapped_column, Mapped,

from datetime import datetime

from app.models.models import Base

from uuid import UUID
class users(Base):
    __tablename__ = "users"
    id: Mapped[UUID] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, onupdate=datetime.utcnow)


