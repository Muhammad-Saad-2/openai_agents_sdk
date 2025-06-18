from LLM.gemini import config
from agents import Runner, set_tracing_disabled
from my_agents.agents import  triage_agent
import chainlit as cl 
from agents import enable_verbose_stdout_logging 

enable_verbose_stdout_logging()

set_tracing_disabled(disabled=True)
#     history.append({"role":"user", "content":message.content})
#     agent_response = await Runner.run(triage_agent, input=history,  run_config=config)

    
#     await cl.Message(
#         content = agent_response.final_output
#     ).send()


async def main():
    response = await Runner.run(triage_agent, input = " what is EBITA in business terms also tell me how many characters is the word 'Deoxyribonucleic' consist of", run_config=config)
    print(response.final_output)



if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
