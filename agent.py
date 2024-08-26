from dotenv import dotenv_values
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_anthropic import ChatAnthropic
from langchain_community.tools import ShellTool
from langchain_core.prompts import ChatPromptTemplate


#Define LLM model
llm = ChatAnthropic(
    model="claude-3-5-sonnet-20240620",
    api_key = dotenv_values(".env")['ANTHROPIC_API_KEY'],
    temperature=0,
    max_tokens=1024,
    timeout=None,
    max_retries=2,
    # other params...
)

# Prompt for creating Tool Calling Agent
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant.",
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)


#Initializa the ShellTool to allow agent to run CLI commands
shell_tool = ShellTool()

tools = [shell_tool]

agent = create_tool_calling_agent(llm, tools, prompt)
# Create an agent executor by passing in the agent and tools
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

#Define CLI PyATS command to run
pyats_command = 'pyats parse "show ip interface brief" --testbet-file testbed.yaml'

#Run the SSH command and handle potential errors
try:
    response = agent_executor.invoke({"input": f'Run this command pyats parse {pyats_command}'})
    print(response)
except Exception as e:
    print(e)

