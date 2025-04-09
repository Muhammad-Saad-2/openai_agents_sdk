import asyncio
from LLM.gemini import config
from agents import Runner, function_tool
from my_agents.math_agent import math_agent
import chainlit as cl 



@cl.on_chat_start
async def on_chat_start():
    cl.user_session.set("history", [])
    await cl.Message(
        content="hello I'm your maths agent, what brings you here"
        ).send()


@cl.on_message
async def main(message: cl.Message):
    history = cl.user_session.get("history")
    history.append({"role":"user", "content":message.content})
    agent_response = await Runner.run(math_agent, input=history,  run_config=config)

    
    await cl.Message(
        content = agent_response.final_output
    ).send()

if __name__ == "__main__":
    pass
