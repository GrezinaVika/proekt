from typing import TYPE_CHECKING

from sqlalchemy import String, Float, ForeignKey, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.database import Base

if TYPE_CHECKING:
    from app.models.waiter_statistics import WaiterStatisticsModel


class WaiterStatisticsModel(Base):
    __tablename__ = "waiter_statistics"
    id: Mapped[int] = mapped_column(primary_key=True)
    waiter_id: Mapped[int] = mapped_column()
    total_orders: Mapped[int] = mapped_column(primary_key=True)
    occupied_tables: Mapped[int] = mapped_column(primary_key=True)
    last_updated: Mapped[int] = mapped_column(String(255), primary_key=True)

    waiter: Mapped["WaiterStatisticsModel"] = relationship(back_populates="waiters")

