from typing import TYPE_CHECKING

from sqlalchemy import String, Float, ForeignKey 
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.database import Base

if TYPE_CHECKING:
    from app.models.orders_items import OrdersItemsModel


class OrdersItemsModel(Base):
    __tablename__ = "orders_items"
    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(primary_key=True, nullable=True)
    menu_id: Mapped[int] = mapped_column(primary_key=True, nullable=True)
    quantity: Mapped[int] = mapped_column(primary_key=True, nullable=True)
    price: Mapped[int] = mapped_column(nullable=False)