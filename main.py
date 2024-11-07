import os
import autogen

CLAUDE_CONFIG = [{
    "model": "claude-3-5-sonnet-20241022",
    "api_key": os.getenv("ANTHROPIC_API_KEY"),
    "api_type": "anthropic"
}]

def create_chat_agents():
    """Initialize and return the AI assistant and user proxy agents."""
    ai_agent = autogen.AssistantAgent(
        name="ai_agent",
        llm_config={"config_list": CLAUDE_CONFIG},
        system_message="You are a helpful AI assistant who can discuss any topic and help with tasks."
    )

    user_agent = autogen.UserProxyAgent(
        name="user",
        human_input_mode="ALWAYS",
        code_execution_config={
            "work_dir": "coding",
            "use_docker": False,
        }
    )
    
    return ai_agent, user_agent

def main():
    """Initialize chat agents and start the conversation."""
    ai_agent, user_agent = create_chat_agents()
    user_agent.initiate_chat(
        ai_agent,
        message="Hello! I'm ready to help you with any questions or tasks you have."
    )

if __name__ == "__main__":
    main()
