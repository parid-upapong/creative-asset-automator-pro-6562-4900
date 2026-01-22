import enum
from sqlalchemy import Column, String, Integer, ForeignKey, Enum, JSON, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid
from app.db.base_class import Base

class AssetStatus(str, enum.Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"

class MasterAsset(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    title = Column(String(255), nullable=False)
    source_url = Column(String(512), nullable=False) # S3 Path
    file_type = Column(String(50)) # video/mp4, audio/mpeg
    
    # Metadata extracted by AI
    technical_metadata = Column(JSON, nullable=True) # duration, resolution, fps
    ai_summary = Column(String, nullable=True)
    
    status = Column(Enum(AssetStatus), default=AssetStatus.PENDING)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), on_update=func.now())