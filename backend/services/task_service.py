
# from tasks.models import Task,CommandHistory
# from tasks.ai_parser import parse_content

# from ai.vector_search import find_similarity

# from tasks.llm_parser import parse_content



# def handle_ai_command(text,user):
#   #last created object ostundhi manaki
#   last_command_obj = CommandHistory.objects.filter(user = user).order_by("-created_at").first()

#   last_command = last_command_obj .command if last_command_obj else ""
  
#   tasks = Task.objects.filter(user=user)
#   task_list = [task.task_texts for task in tasks]

#   result = parse_content(text=text,last_command=last_command,task_list=task_list)

#   action = result.get("action")
#   task_text = result.get("task")

#   CommandHistory.objects.create(user=user,command=text)


  
#   if action =="create":
#     task = Task.objects.create(task_texts = task_text,user=user)
#     return {"message" : "Task create chesa lera babu","task" : task.task_texts}
  
#   if not task_list:
#     return {"message" :"No tasks Available"}


#   matched_task = find_similarity(task_text,task_list)

#   if action == "delete":
#     task = Task.objects.filter(task_texts = matched_task,user=user).first()
#     if task:
#       task.delete()

#       return {"message":"Task Delete chesan le ","task" : matched_task}

#   if action == "update":
#     task = Task.objects.filter(
#             task_texts=matched_task,
#             user=user
#         ).first()
#     if task:
#       task.status = True
#       task.save()

#       return {"message" : "Task Complete chesav","task" : matched_task}
  
#     return {"message" : "No matching Task"}


#   # if action == "create":

#   #   task = Task.objects.create(task_texts = text,user=user)
#   #   return {"message" : "Task create chesan ra babu",
#   #           "task" : task.task_texts}
#   # return result
from tasks.models import Task, CommandHistory
from tasks.llm_parser import parse_content
from ai.vector_search import find_similarity


def handle_ai_command(text, user):

    # 1) fetch previous command memory
    last_command_obj = CommandHistory.objects.filter(
        user=user
    ).order_by("-created_at").first()

    last_command = last_command_obj.command if last_command_obj else ""

    # 2) fetch existing tasks
    tasks = Task.objects.filter(user=user)
    task_list = [task.task_texts for task in tasks]

    # 3) let LLM understand current sentence using memory
    result = parse_content(
        text=text,
        last_command=last_command,
        task_list=task_list
    )

    action = result.get("action")
    task_text = result.get("task")

    # 4) save current command for future memory
    CommandHistory.objects.create(
        user=user,
        command=text
    )

    # 5) create new task
    if action == "create":
        task = Task.objects.create(
            task_texts=task_text,
            user=user
        )

        return {
            "message": f"Task created successfully: {task.task_texts}",
            "task": task.task_texts
        }

    # 6) safety for empty tasks
    if not task_list:
        return {"message": "No tasks available"}

    # 7) semantic task matching
    matched_task = find_similarity(task_text, task_list)

    # 8) delete flow
    if action == "delete":
        task = Task.objects.filter(
            task_texts=matched_task,
            user=user
        ).first()

        if task:
            task.delete()
            return {
                "message": f"Task deleted successfully: {matched_task}",
                "task": matched_task
            }

    # 9) update flow
    if action == "update":
        task = Task.objects.filter(
            task_texts=matched_task,
            user=user
        ).first()

        if task:
            task.status = True
            task.save()

            return {
                "message": f"Task completed successfully: {matched_task}",
                "task": matched_task
            }

        return {"message": "No matching task found"}

    return {"message": "Invalid action"}