from langchain_openai.chat_models import AzureChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage

tools = [TavilySearchResults(max_results=2)]

graph = create_react_agent(model, tools)

# final_state = graph.invoke(
#     {"messages": [HumanMessage(content="爱因斯坦的人生经历？")]},
# )

# print(final_state)
