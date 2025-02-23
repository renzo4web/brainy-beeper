from bot.service.database import db
from models import User


def extract_user_intention(intention, todo_id=0, todo_title="", todo_content="", user=User):
    print("tool[extract_user_intention]", intention, todo_id, todo_title)
    if intention == "CREATE_TODO":
        # Handle create todo
        print("Creating todo", todo_title, todo_content, user.id)
        db.create_todo(title=todo_title, content=todo_content, user_id=user.id)
        return f"Todo {todo_title} created"
    elif intention == "MARK_TODO_AS_DONE":
        db.update_todo(todo_id=todo_id, is_completed=True)
        return f"MARK A TODO WITH ID {todo_id} AS DONE"
    elif intention == "DELETE_TODO":
        return f"DELETE A TODO WITH ID {todo_id}"
    elif intention == "LIST_TODOS":
        return "LIST TODOS"


extract_user_intention_tool = {
    "type": "function",
    "function": {
        "name": "extract_user_intention",
        "description": "Extract the user intention of what they want to do from the message, can be CREATE_TODO (the user want to complete some task in the future), MARK_TODO_AS_DONE (the user want to mark a task as done, the task should be in the context message), DELETE_TODO (the user want to delete a task), LIST_TODOS (the user want to list all tasks).",
        "parameters": {
            "type": "object",
            "properties": {
                "intention": {
                    "type": "string",
                    "description": "The intention of the user. Valid intentions are CREATE_TODO (the user want to complete some task in the future can be anything), MARK_TODO_AS_DONE (the user want to mark a task as done, the task should be in the context message), DELETE_TODO (the user want to delete a specific task and his reference a todo NOT a task), LIST_TODOS (the user want to list all tasks)."
                },
                "todo_id": {
                    "type": "number",
                    "description": "The id of the todo to edit or delete. This is only required if the intention is DELETE_TODO, otherwise it should be 0."
                },
                "todo_title": {
                    "type": "string",
                    "description": "The title of the todo should be a short sentence that summarizes the task max 3 words. This is only required if the intention is CREATE_TODO, otherwise it should be an empty string."
                },
                "todo_content": {
                    "type": "string",
                    "description": "The user message content, do not modify this, only used when CREATE_TODO. otherwise it should be an empty string."
                }
            },
            "required": [
                "intention",
                "todo_id",
                "todo_title",
                "todo_content"
            ],
            "additionalProperties": False
        },
        "strict": True
    }
}


tools = [extract_user_intention_tool]

def get_tools():
    return tools
