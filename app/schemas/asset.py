from pydantic import BaseModel, HttpUrl
from uuid import UUID
from datetime import datetime
from typing import Optional, Any

class AssetBase(BaseModel):
    title: str

class AssetCreate(AssetBase):
    source_url: str
    user_id: UUID

class AssetUpdate(BaseModel):
    status: Optional[str]
    ai_summary: Optional[str]
    technical_metadata: Optional[dict]

class AssetResponse(AssetBase):
    id: UUID
    user_id: UUID
    status: str
    source_url: str
    created_at: datetime

    class Config:
        from_attributes = True