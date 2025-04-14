from agents import Agent, handoff
from LLM.gemini import model
from tools.weather_tool import get_weather

weather_agent = Agent(
    name = "weather agent",
    instructions = "you are a weather agent that tells people the weater of whatever place they ask and help them with wether queries",
    model = model,
    tools = [get_weather]

)

math_agent = Agent(
    name="math agent",
    instructions="you're an expert math agent having expertise in all areas of maths, especially built to solve complex maths problems",
    model=model

)

triage_agent = Agent(
    name = "triage_agent",
    instructions="you're a triage agent your task is to determine the user's prompt and select the appropriate agent to fullfill the task",
    model=model,
    handoffs=[math_agent, weather_agent]
)
