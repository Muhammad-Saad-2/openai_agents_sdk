from agents import function_tool

#creating a fake tool
@function_tool
def get_weather(city: str) -> str:
    return f"the weather in {city} is sunny"
