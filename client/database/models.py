from .db import Base
from sqlalchemy import Column, Integer, String, TEXT


class Setting(Base):
    __tablename__ = 'settings'

    setting_id = Column(Integer(), primary_key=True)
    setting_name = Column(String(80), nullable=False)
    setting_value = Column(TEXT, nullable=False)
