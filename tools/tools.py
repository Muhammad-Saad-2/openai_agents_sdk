from agents import function_tool

#creating a fake tool
@function_tool
def get_weather(city: str) -> str:
    return f"the weather in {city} is sunny"


@function_tool
def count_char(word:str):
    count  = 0
    for char in word:
        if char.isalpha():
            count += 1
    return count
    





        

