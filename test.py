from  tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights
from backend import run_travel_agent
from langchain_core.messages import AnyMessage

# res = tavily_search("Best travel destinations in Europe")
# print(res)

# res = search_flights("Plan a 7 days trip from Bangalore to Nepal")
# print(res)

response = run_travel_agent("Plan a 7 days trip from Bangalore to Nepal")
print(response)