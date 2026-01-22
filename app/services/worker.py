from celery import Celery
from app.core.config import settings

celery_app = Celery("tasks", broker=settings.CELERY_BROKER_URL)
celery_app.conf.update(
    result_backend=settings.CELERY_RESULT_BACKEND,
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
)

@celery_app.task(name="pipeline.process_master_asset")
def process_master_asset_task(asset_id: str):
    """
    Entry point for the AI Pipeline.
    Triggered after successful upload.
    1. Triggers Transcription Agent
    2. Triggers CV Pipeline for scene detection
    3. Updates Asset status in DB
    """
    # Logic is implemented in the worker service
    print(f"Starting AI Orchestration for asset: {asset_id}")
    return {"status": "triggered", "asset_id": asset_id}