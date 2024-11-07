import os

import autogen

config_list_claude = [
    {
        "model": "claude-3-5-sonnet-20241022",
        "api_key": os.getenv("ANTHROPIC_API_KEY"),
        "api_type": "anthropic"
    }
]

# Create the AI assistant
assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config={
        "config_list": config_list_claude,
    },
    system_message="You are a helpful AI assistant who can discuss any topic and help with tasks."
)

# Create the human user proxy
user_proxy = autogen.UserProxyAgent(
    name="human",
    human_input_mode="ALWAYS",  # Always get input from the human
    code_execution_config={
        "work_dir": "coding",
        "use_docker": False,
    }
)

# Start the conversation
user_proxy.initiate_chat(
    assistant,
    message="Hello! I'm ready to help you with any questions or tasks you have."
)
