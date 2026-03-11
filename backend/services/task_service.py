from tasks.models import Task
from tasks.ai_parser import parse_content

from ai.vector_search import find_similarity
from tasks.models import Task
from tasks.ai_parser import parse_content



def handle_ai_command(text,user):
  result = parse_content(text)
  action = result.get("action")
  
  if action =="create":
    task = Task.objects.create(task_texts = task,user=user)
    return {"messag" : "Task create chesa lera babu","task" : task.task_texts}
  
  tasks = Task.objects.filter(user=user)
  task_list = [task.task_texts for task in tasks]

  matched_task = find_similarity(task,task_list)

  if action == "delete":
    task = 


  # if action == "create":

  #   task = Task.objects.create(task_texts = text,user=user)
  #   return {"message" : "Task create chesan ra babu",
  #           "task" : task.task_texts}
  # return result
