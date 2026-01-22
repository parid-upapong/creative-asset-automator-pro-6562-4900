from typing import Dict, Any
from .base import BaseAgent

class BrandGuardianAgent(BaseAgent):
    """The Brand Guardian: Ensures all outputs match the brand identity."""

    async def process(self, generated_content: Dict[str, Any]) -> Dict[str, Any]:
        self.log_action(f"Auditing content for {generated_content['platform']}")
        
        prohibited_words = self.brand_config.get("prohibited_words", [])
        content_text = generated_content["generated_text"]
        
        # Check for brand violations
        violations = [word for word in prohibited_words if word.lower() in content_text.lower()]
        
        if violations:
            return {
                "is_approved": False,
                "reason": f"Found prohibited words: {violations}",
                "action": "REGENERATE"
            }
            
        return {
            "is_approved": True,
            "reason": "Aligned with Brand Kit",
            "action": "PROCEED"
        }