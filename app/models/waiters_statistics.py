from typing import TYPE_CHECKING

from sqlalchemy import String, Float, ForeignKey, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.database import Base

if TYPE_CHECKING:
    from app.models.waiters_statistics import WaitersStatisticsModel


class WaiterStatisticsModel(Base):
    __tablename__ = "waiters_statistics"
    id: Mapped[int] = mapped_column(primary_key=True)
    waiter_id: Mapped[int] = mapped_column(primary_key=True)
    total_orders: Mapped[int] = mapped_column(primary_key=True)
    occupied_tables: Mapped[int] = mapped_column(primary_key=True)
    last_updated: Mapped[VARCHAR] = mapped_column(String(255), nullable=True)

    waiter_id: Mapped[list["WaitersModel"]] = relationship(back_populates="waiters")
