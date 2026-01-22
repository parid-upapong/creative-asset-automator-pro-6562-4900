from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID
from typing import List

from app.db.session import get_db
from app.models.asset import MasterAsset
from app.schemas.asset import AssetCreate, AssetResponse
from app.services.worker import process_master_asset_task

router = APIRouter()

@router.post("/", response_model=AssetResponse)
def create_asset(asset_in: AssetCreate, db: Session = Depends(get_db)):
    """
    Register a new Master Asset and trigger the AI processing pipeline.
    """
    new_asset = MasterAsset(
        title=asset_in.title,
        user_id=asset_in.user_id,
        source_url=asset_in.source_url
    )
    db.add(new_asset)
    db.commit()
    db.refresh(new_asset)
    
    # Trigger Asynchronous AI Pipeline
    process_master_asset_task.delay(str(new_asset.id))
    
    return new_asset

@router.get("/{asset_id}", response_model=AssetResponse)
def get_asset(asset_id: UUID, db: Session = Depends(get_db)):
    asset = db.query(MasterAsset).filter(MasterAsset.id == asset_id).first()
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    return asset