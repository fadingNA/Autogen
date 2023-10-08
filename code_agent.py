from autogen import config_list_from_json
import autogen

config_list = config_list_from_json(env_or_file='OAI_CONFIG.json')
llm_config = {
    "config_list": config_list,
    "seed": 42,
    "request_timeout": 100,
}

user_proxy = autogen.UserProxyAgent(name='UserProxy', 
                                    system_message="A human admin who will give the idea and run the code provided by Coder.",
                                    code_execution_config={"last_n_messages": 2, "work_dir": "group_chat"},
                                    human_input_mode="ALWAYS",)

coder = autogen.AssistantAgent(
    name='Coder', 
    llm_config=llm_config
)

project_manager = autogen.AssistantAgent(
    name='ProjectManager', 
    system_message="You will help me break down the project into smaller tasks and assign them to the team members.",
    llm_config=llm_config
)

groupchat = autogen.GroupChat(
    agents=[user_proxy, coder, project_manager], messages=[]
)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

user_proxy.initiate_chat(manager, message="Build a classic & basic ASP.NET MVC application. query the data")

