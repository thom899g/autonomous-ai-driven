import logging
from typing import Optional, Dict, Any
from perception_module import PerceptionModule
from decision_making_agent import DecisionMakingAgent
from communication_layer import CommunicationLayer
from learning_engine import LearningEngine

class IntegrationBridge:
    def __init__(self):
        self.logger = logging.getLogger("IntegrationBridge")
        self.logger.setLevel(logging.INFO)
        self.perception = PerceptionModule()
        self.decision_maker = DecisionMakingAgent()
        self.communication = CommunicationLayer()
        self.learning = LearningEngine()
        
    def process_data(self, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Processes and routes data through the system.
        
        Args:
            data: Input data to be processed.
            
        Returns:
            Processed result or None if processing fails.
        """
        try:
            self.logger.info("Starting data processing pipeline")
            
            # Step 1: Perception
            perception_result = self.perception.process_image(data.get("image_path"))
            if not perception_result:
                raise Exception("Perception failed")
                
            # Step 2: Decision Making
            decision = self.decision_maker.make_decision(perception_result)
            if not decision:
                raise Exception("Decision making failed")
                
            # Step 3: Communication
            communication_result = self.communication.send_message(
                decision, data.get("endpoint"))
            if not communication_result:
                raise Exception("Communication failed")
                
            # Step 4: Learning
            if not self.learning.train_model(communication_result):
                raise Exception("Learning failed")
                
            return {
                "status": "success",
                "result": communication_result
            }
            
        except Exception as e:
            self.logger.error(f"Data processing pipeline failed: {str(e)}")
            return None
            
    def __repr__(self) -> str:
        return "Integration Bridge for coordinating system operations"