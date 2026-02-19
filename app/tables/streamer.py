from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Streamer(Base):
    __tablename__ = "streamers"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, unique=True, index=True)
    main_contents = Column(ARRAY(String), nullable=True)

    group_id = Column(Integer, ForeignKey("groups.id"), nullable=True)
    group = relationship("Group", back_populates="streamers")

    platform_id = Column(Integer, ForeignKey("platforms.id"), nullable=False)
    platform = relationship("Platform", back_populates="streamers")