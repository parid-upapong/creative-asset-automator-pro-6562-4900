from abc import ABC, abstractmethod
from typing import Any, Dict
import logging

class BaseAgent(ABC):
    """Base class for all Project OVERLORD agents."""
    
    def __init__(self, agent_name: str, brand_config: Dict[str, Any]):
        self.agent_name = agent_name
        self.brand_config = brand_config
        self.logger = logging.getLogger(f"overlord.{agent_name}")

    @abstractmethod
    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Core logic for the agent's task."""
        pass

    def log_action(self, message: str):
        self.logger.info(f"[{self.agent_name}] {message}")