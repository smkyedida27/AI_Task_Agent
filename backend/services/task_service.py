from tasks.models import Task
from tasks.ai_parser import parse_content


def handle_ai_command(text,user):
  result = parse_content(text)
  action = result.get("action")


  if action == "create":

    task = Task.objects.create(task_texts = text,user=user)
    return {"message" : "Task create chesan ra babu",
            "task" : task.task_texts}
  return result
