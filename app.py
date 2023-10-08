from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

# Import config
config_list = config_list_from_json('OAI_CONFIG.json')

# Create agents

assistant = AssistantAgent(name='Non', llm_config={
    'config_list': config_list,
})


# create user proxy agent

user_proxy = UserProxyAgent(name='UserProxy', code_execution_config={"work_dir": "coding"})


user_proxy.initiate_chat(assistant, message="")
                            
                        