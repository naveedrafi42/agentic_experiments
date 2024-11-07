import os
import autogen

CLAUDE_CONFIG = [{
    "model": "claude-3-5-sonnet-20241022",
    "api_key": os.getenv("ANTHROPIC_API_KEY"),
    "api_type": "anthropic"
}]

class DataAnalystAgent:
    def __init__(self):
        self.ai_agent = autogen.AssistantAgent(
            name="data_analyst",
            llm_config={"config_list": CLAUDE_CONFIG},
            system_message="You are a helpful data analyst AI assistant who can analyze data and provide insights."
        )
        self.current_focus = "Ready to analyze data"
        self.confidence_level = 95
        self.processing_mode = "Active listening"

    def process_message(self, message):
        # Use the AI agent to process the message
        response = self.ai_agent.generate_response(message)
        
        # Update state based on processing
        self.current_focus = f"Analyzing: {message[:30]}..."
        
        return {
            'response': response,
            'current_focus': self.current_focus,
            'confidence_level': self.confidence_level,
            'processing_mode': self.processing_mode
        }

def create_agent():
    return DataAnalystAgent()

if __name__ == "__main__":
    agent = create_agent()
