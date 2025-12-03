from typing import TYPE_CHECKING

from sqlalchemy import String, Float, ForeignKey, DATETIME
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.database import Base
from app.models.tables import TablesModel

if TYPE_CHECKING:
    from app.models.cook import cookModel


class cookModel(Base):
    __tablename__ = "cook"
    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[int] = mapped_column(primary_key=True, nullable=True)
    password: Mapped[int] = mapped_column(primary_key=True, nullable=True)
    role: Mapped[int] = mapped_column(primary_key=True, nullable=True)
    last_login: Mapped[DATETIME] = mapped_column(String(255), nullable=False, default="Создан")
    
table: Mapped["OrdersModel"] = relationship(back_populates="tables")
