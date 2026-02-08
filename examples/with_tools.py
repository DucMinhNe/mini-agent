from mini_agent import Agent
from mini_agent.tools import SearchTool, CalculatorTool

print(Agent(tools=[SearchTool(), CalculatorTool()]).run('search and compute'))
