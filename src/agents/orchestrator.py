import asyncio
from typing import List, Dict, Any
from .base import BaseAgent
from .curator import CuratorAgent
from .ghostwriter import GhostwriterAgent

class OrchestratorAgent(BaseAgent):
    """The Architect: Routes tasks between specialized agents."""

    async def process(self, project_data: Dict[str, Any]) -> Dict[str, Any]:
        self.log_action(f"Starting orchestration for Project: {project_data['project_id']}")
        
        # 1. Analyze Content (The Curator)
        curator = CuratorAgent(self.brand_config)
        analysis_results = await curator.process({
            "transcript": project_data["transcript"],
            "duration": project_data["duration"]
        })

        # 2. Parallel Generation (The Ghostwriter & The Visualist)
        tasks = []
        for segment in analysis_results["high_impact_segments"]:
            tasks.append(self.generate_platform_content(segment))
        
        final_assets = await asyncio.gather(*tasks)
        
        return {
            "status": "COMPLETED",
            "assets": final_assets
        }

    async def generate_platform_content(self, segment: Dict[str, Any]) -> Dict[str, Any]:
        ghostwriter = GhostwriterAgent(self.brand_config)
        return await ghostwriter.process(segment)