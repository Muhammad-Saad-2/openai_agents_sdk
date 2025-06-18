from agents import OpenAIChatCompletionsModel, AsyncOpenAI, set_default_openai_api, set_default_openai_client
from agents.run import RunConfig
from LLM.settings import api_key

set_default_openai_api("chat_completions")

external_client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    
 )

set_default_openai_client(external_client)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=False

)