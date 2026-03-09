from django.urls import path
from .views import get_tasks,post_tasks,update_tasks,delete_task,ai_command



urlpatterns = [

  path('tasks/',get_tasks),
  path('tasks/create/',post_tasks),
  path('tasks/update/<int:id>/',update_tasks),
  path('tasks/deletee/<int:id>/',delete_task),

  path('ai_command/',ai_command),
]