from agents import Agent, Runner, function_tool
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from LLM.gemini import model, config
import chainlit as cl
from tools.weather_tool import get_weather



weather_agent = Agent(
    name = "weather agent",
    instructions = "you are a weather agent that tells people the weater of whatever place they ask and help them with wether queries",
    model = model,
    tools = [get_weather]

)

@cl.on_message
async def run_weather_agent(message: cl.Message):
    history = [{"role": "user", "content": message.content}]
    result = await Runner.run(weather_agent, input=history, run_config=config)
    await cl.Message(
        content=result.final_output
    ).send()