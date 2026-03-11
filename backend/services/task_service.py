
from tasks.models import Task
from tasks.ai_parser import parse_content

from ai.vector_search import find_similarity




def handle_ai_command(text,user):
  result = parse_content(text)
  action = result.get("action")
  task_text = result.get("task")
  
  if action =="create":
    task = Task.objects.create(task_texts = task_text,user=user)
    return {"message" : "Task create chesa lera babu","task" : task.task_texts}
  
  tasks = Task.objects.filter(user=user)
  task_list = [task.task_texts for task in tasks]

  matched_task = find_similarity(task_text,task_list)

  if action == "delete":
    task = Task.objects.filter(task_texts = matched_task,user=user).first()
    if task:
      task.delete()

      return {"message":"Task Delete chesan le ","task" : matched_task}

  if action == "update":
    task = Task.objects.filter(
            task_texts=matched_task,
            user=user
        ).first()
    if task:
      task.status = True
      task.save()

      return {"message" : "Task Complete chesav","task" : matched_task}
  
    return {"message" : "No matching Task"}


  # if action == "create":

  #   task = Task.objects.create(task_texts = text,user=user)
  #   return {"message" : "Task create chesan ra babu",
  #           "task" : task.task_texts}
  # return result
