from typing import TYPE_CHECKING

from sqlalchemy import String, Float, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.database import Base

if TYPE_CHECKING:
    from app.models.waiter import WaiterModel


class WaiterModel(Base):
    __tablename__ = "Waiter"
    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[int] = mapped_column(primary_key=True, nullable=True)
    password: Mapped[int] = mapped_column(primary_key=True, nullable=True)
    role: Mapped[int] = mapped_column(primary_key=True, nullable=True)
    last_login: Mapped[DateTime] = mapped_column(String(255), nullable=True)

