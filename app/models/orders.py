from typing import TYPE_CHECKING

from sqlalchemy import String, Float, ForeignKey,  Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.database import Base

if TYPE_CHECKING:
    from app.models.orders import OrdersModel


class OrdersModel(Base):
    __tablename__ = "orders"
    id: Mapped[int] = mapped_column(primary_key=True)
    table_id: Mapped[int] = mapped_column(primary_key=True, nullable=True)
    cook_id: Mapped[int] = mapped_column(primary_key=True, nullable=True)
    waiter_id: Mapped[int] = mapped_column(primary_key=True, nullable=True)
    status: Mapped[str] = mapped_column(String(255), nullable=False, default="Создан")
    

