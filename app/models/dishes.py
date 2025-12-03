from typing import TYPE_CHECKING

from sqlalchemy import String, Float, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.database import Base

if TYPE_CHECKING:
    from app.models.dishes import DishesModel


class DishesModel(Base):
    __tablename__ = "dishes"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[int] = mapped_column(primary_key=True, nullable=True)
    description: Mapped[str] = mapped_column(String(250), nullable=True)
    price: Mapped[int] = mapped_column(primary_key=True, nullable=True)
    category_id: Mapped[int] = mapped_column(primary_key=True, nullable=True)
    admin_id: Mapped[int] = mapped_column(primary_key=True, nullable=True)

category: Mapped["DishesModel"] = relationship(back_populates="category")
admin: Mapped["DishesModel"] = relationship(back_populates="admin")