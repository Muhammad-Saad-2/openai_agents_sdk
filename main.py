import asyncio
from LLM.gemini import config
from agents import Runner
from my_agents.math_agent import math_agent
import chainlit as cl 


@cl.on_message
async def main(message: cl.Message):
    agent_response = await Runner.run(math_agent, input=message.content,  run_config=config)
    
    await cl.Message(
        content = agent_response.final_output
    ).send()

if __name__ == "__main__":
    asyncio.run (main())
    pass
