from typing import TYPE_CHECKING

from sqlalchemy import String, Float, ForeignKey 
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.database import Base

if TYPE_CHECKING:
    from app.models.categories import CategoriesModel


class CategoriesModel(Base):
    __tablename__ = "categories"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[int] = mapped_column(primary_key=True, nullable=True)
    discription: Mapped[str] = mapped_column(String(250), nullable=True)