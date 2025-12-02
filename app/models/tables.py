from typing import TYPE_CHECKING

from sqlalchemy import String, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.database import Base

if TYPE_CHECKING:
    from app.models.tables import TablesModel


class TablesModel(Base):
    __tablename__ = "tables"

    id: Mapped[int] = mapped_column(primary_key=True)
    table_number: Mapped[int] =  mapped_column(primary_key=True, nullable=True)
    status: Mapped[VARCHAR] = mapped_column(String(255), nullable=True)
