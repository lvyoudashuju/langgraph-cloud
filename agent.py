from langchain_openai.chat_models import AzureChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage

import os
os.environ['OPENAI_API_VERSION'] = '2024-04-01-preview'
os.environ['AZURE_OPENAI_ENDPOINT'] = 'https://jiarong.openai.azure.com/'
os.environ['AZURE_OPENAI_API_KEY'] = '9fe6fef3704644729317f2eb57e2fad7'
os.environ["TAVILY_API_KEY"] = "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"
LANGSMITH_TRACING = True
os.environ["LANGSMITH_API_KEY"] = "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"

model = AzureChatOpenAI(azure_deployment='category_agent_summary')

tools = [TavilySearchResults(max_results=2)]

graph = create_react_agent(model, tools)

# final_state = graph.invoke(
#     {"messages": [HumanMessage(content="爱因斯坦的人生经历？")]},
# )

# print(final_state)