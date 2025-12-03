from typing import TYPE_CHECKING

from sqlalchemy import String, Float, ForeignKey, DateTime, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.database import Base

if TYPE_CHECKING:
    from app.models.cook_statistics import CookStatisticsModel


class CookStatisticsModel(Base):
    __tablename__ = "cook_statistics"
    id: Mapped[int] = mapped_column(primary_key=True)
    cook_id: Mapped[int] = mapped_column(Integer, nullable=True)
    ative_orders: Mapped[int] = mapped_column(Integer, nullable=True)
    

cook: Mapped["CookStatisticsModel"] = relationship(back_populates= "cook")