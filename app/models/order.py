from typing import TYPE_CHECKING

from sqlalchemy import String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.database import Base
from app.models.tables import TablesModel

if TYPE_CHECKING:
    from app.models.order import OrderModel


class OrderModel(Base):
    __tablename__ = "order"
    id: Mapped[int] = mapped_column(primary_key=True)
    table_id: Mapped[int] = mapped_column(primary_key=True, nullable=True)
    cook_id: Mapped[int] = mapped_column(primary_key=True, nullable=True)
    waiters_id: Mapped[int] = mapped_column(primary_key=True, nullable=True)
    status: Mapped[str] = mapped_column(String(255), nullable=False, default="Создан")
    
    table: Mapped["OrderModel"] = relationship(back_populates="tables")
    waiters: Mapped["OrderModel"] = relationship(back_populates="waiters")
    cook: Mapped["OrderModel"] = relationship(back_populates="cook")