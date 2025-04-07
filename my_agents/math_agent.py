from agents import Agent
from LLM.gemini import model

math_agent = Agent(
    name="math agent",
    instructions="you're an expert math agent having expertise in all areas of maths, especially built to solve complex maths problems",
    model=model

)