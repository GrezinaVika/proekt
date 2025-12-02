from typing import TYPE_CHECKING

from sqlalchemy import String, Float, ForeignKey, VARCHAR, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.database import Base

if TYPE_CHECKING:
    from app.models.Waiters import WaitersModel


class UserModel(Base):
    __tablename__ = "Waiters"
    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[VARCHAR] = mapped_column(String(255), nullable=True)
    password: Mapped[VARCHAR] = mapped_column(String(255), nullable=True)
    role: Mapped[VARCHAR] = mapped_column(String(255), nullable=True)
    last_login: Mapped[DateTime] = mapped_column(String(255), nullable=True)

