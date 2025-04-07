import asyncio
from LLM.gemini import config
from agents import Runner
from my_agents.math_agent import math_agent

def main():
    agent_response = Runner.run_sync(math_agent, "what would be the factorial of 4", run_config=config)
    print(agent_response.final_output)

if __name__ == "__main__":
    main()
