import logging
from typing import Optional, Dict, Any
import requests

class CommunicationLayer:
    def __init__(self):
        self.logger = logging.getLogger("CommunicationLayer")
        self.logger.setLevel(logging.INFO)
        
    def send_message(self, message: Dict[str, Any], endpoint: str) -> Optional[Dict[str, Any]]:
        """
        Sends a message to the specified endpoint.
        
        Args:
            message: Message data to be sent.
            endpoint: URL of the receiver service.
            
        Returns:
            Response from the server or None if sending fails.
        """
        try:
            self.logger.info(f"Sending message to {endpoint}")
            response = requests.post(endpoint, json=message)
            if response.status_code == 200:
                return response.json()
            else:
                raise Exception(f"Failed to send message. Status code: {response.status_code}")
                
        except Exception as e:
            self.logger.error(f"Communication failed: {str(e)}")
            return None
            
    def __repr__(self) -> str:
        return "Communication Layer for data exchange"