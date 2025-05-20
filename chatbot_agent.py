import ollama
from tools import calculator, file_reader, weather, opsera_doc_search
import json

def classify_with_llama3(user_input: str) -> dict: # define function that will take a string as an argument and return a dictionary. 
    # create a multiline f string that feeds a prompt to the ollama3 LLM, telling it to choose between prompts when given an input. 
    # have it return the file in a specific json format.
    prompt = f"""
You are a tool-routing assistant. You must choose one of the following tools: "calculator", "weather", "file_reader", or "opsera_doc_search".

Given a user input, respond with only a JSON object in this format:
{{"tool": "<tool_name>", "argument": "<relevant_text>"}}

For example:
User: "what is 4 + 5"
-> {{"tool": "calculator", "argument": "4 + 5"}}

User: "what’s the weather in San Francisco?"
-> {{"tool": "weather", "argument": "San Francisco"}}

User: "please read my notes.txt file"
-> {{"tool": "file_reader", "argument": "notes.txt"}}

User: "what is continuous integration in opsera"
-> {{"tool": "opsera_doc_search", "argument": "continuous integration in opsera"}}

Now classify this input:
"{user_input}"
Respond only with valid JSON.
"""
# feed the prompt to ollama and store the response. 
    response = ollama.chat(
        model='llama3',
        messages=[{'role': 'user', 'content': prompt}]
    )

    # print("Raw model response:\n", response['message']['content'])

    try: # attempt to parse the model's JSON output into a python dictionary. 
        result = json.loads(response['message']['content'])
        return result # if successful return the dictionary. 
    except Exception as e: # fallback dictionary returned if unable to parse into a python dictionary. 
        return {"tool": "error", "argument": f"Invalid response: {e}"}

# Route the command to the appropriate tool
def route_command(user_input: str) -> str:
    tool_data = classify_with_llama3(user_input) # store the ollama dictionary.
    tool = tool_data.get("tool") # retrieve the 'tool' key from the given dictionary and store it in variable 'tool'.
    arg = tool_data.get("argument", "") # retreive the 'argument' key from the dictionary and store it in variable 'arg'.

    # route the argument to the correct tool. 
    if tool == "calculator":
        return calculator.calculate(arg)
    elif tool == "weather":
        return weather.weather_lookup(arg)
    elif tool == "file_reader":
        return file_reader.read_file(arg)
    elif tool == "opsera_doc_search":
        return opsera_doc_search.search_opsera_docs(arg)
    else:
        return f"Could not route given command. Reason: {arg}"




