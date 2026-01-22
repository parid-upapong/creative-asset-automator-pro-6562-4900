"""
Service Orchestrator: Handles the logic of breaking down a Master Asset
into multiple sub-tasks for the AI Workers.
"""

import uuid
from typing import List

class TransformationOrchestrator:
    def __init__(self, db, queue):
        self.db = db
        self.queue = queue

    async def start_asset_pipeline(self, user_id: str, asset_url: str, targets: List[str]):
        # 1. Create Project Record
        project_id = str(uuid.uuid4())
        await self.db.projects.create(
            id=project_id,
            user_id=user_id,
            original_url=asset_url,
            status="PROCESSING"
        )

        # 2. Dispatch Ingestion Task (Download & Transcribe)
        ingestion_payload = {
            "project_id": project_id,
            "action": "INGEST_AND_TRANSCRIBE",
            "url": asset_url
        }
        self.queue.push("ingestion_queue", ingestion_payload)

        # 3. Logic continues in Workers via Event Listeners...
        return {"project_id": project_id, "status": "queued"}

    async def on_transcription_complete(self, project_id: str, transcript: str):
        # Triggered by worker webhook
        # Dispatch Content Adaptation Tasks (TikTok, LinkedIn, etc.)
        adaptation_tasks = ["TIKTOK_CLIPPER", "LINKEDIN_POST_GEN", "SUMMARY_GEN"]
        
        for task in adaptation_tasks:
            self.queue.push("adaptation_queue", {
                "project_id": project_id,
                "task_type": task,
                "data": transcript
            })