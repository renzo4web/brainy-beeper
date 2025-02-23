from openai import ChatCompletion
from bot.service.tools import extract_user_intention
import json
from models import User

def call_fn_from_tool_response(completion: ChatCompletion, user: User):
    print("calling fn from tool response")
    print(completion.choices[0].message.tool_calls)
    has_tool_call = completion.choices[0].message.tool_calls is not None
    if not has_tool_call:
        return

    for tool_call in completion.choices[0].message.tool_calls:
        if tool_call.function.name == "extract_user_intention":
            print("extracting user intention")
            arguments = json.loads(tool_call.function.arguments)
            todo_id = int(arguments["todo_id"])  # Convert string to int
            return extract_user_intention(arguments["intention"], todo_id, arguments["todo_title"], arguments["todo_content"], user)
            

    
