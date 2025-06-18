from agents import Agent, handoffs
from LLM.gemini import model
from tools.tools import count_char
from dataclasses import dataclass
import uuid



char_count = Agent(
    name = "Character counter",
    instructions = "you're the agent that counts the number of characters in a given words",
    tools = [count_char]

)

"""call the count_char method if given any word to find the number of characters"""

finance_agent = Agent(
    name = "finance agent",
    instructions = "you're a finance agent that helps user with their financial operations and guide the user throughout their financial queries, read and summarize financial data if any provided, make sure you do not provide any financial investement decisions but instead provide advices with a caution disclaimer that user shall take any further step on their own risk ,",
    model = model,
    input_guardrails = " only reply to the finance related queries",
    handoffs = [char_count],
    handoff_description = "pass the handoff to the char count agent if given the task to count the characters "

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
    handoffs=[math_agent, finance_agent, char_count]
)
