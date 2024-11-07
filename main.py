import os

from autogen import ConversableAgent
import autogen

config_list_claude = [
    {
        # Choose your model name.
        "model": "claude-3-5-sonnet-20241022",
        # You need to provide your API key here.
        "api_key": os.getenv("ANTHROPIC_API_KEY"),
        "api_type": "anthropic"
    }
]

assistant = autogen.AssistantAgent(
    "assistant",
    llm_config={
        "config_list": config_list_claude,
    },
)

user_proxy = autogen.UserProxyAgent(
    "user_proxy",
    human_input_mode="NEVER",
    code_execution_config={
        "work_dir": "coding",
        "use_docker": False,
    },
    is_termination_msg=lambda x: x.get("content", "") and x.get("content", "").rstrip().endswith("TERMINATE"),
    max_consecutive_auto_reply=3,
)

Nadalee = ConversableAgent(
    "Nadalee",
    llm_config={"config_list": config_list_claude},
    system_message="You are an Irish girl planning a honey moon with your Pakistani husband",
    code_execution_config=False,  # Turn off code execution, by default it is off.
    function_map=None,  # No registered functions, by default it is None.
    human_input_mode="NEVER",  # Never ask for human input.
)

Naveed = ConversableAgent(
    "Naveed",
    llm_config={"config_list": config_list_claude},
    system_message="You are a Pakistani man planning your honey moon with an Irish wife whilst coding an agentic system",
    code_execution_config=False,  # Turn off code execution, by default it is off.
    function_map=None,  # No registered functions, by default it is None.
    human_input_mode="NEVER",  # Never ask for human input.
)

result = Nadalee.initiate_chat(Naveed, message="Look up this glamping place in thailand", max_turns=2)

# reply = agent.generate_reply(messages=[{"content": "Whats the weather in Edinburgh?", "role": "user"}])
# print(reply)

# user_proxy.initiate_chat(
#     assistant, message="Write a script for the shortest comedy"
# )