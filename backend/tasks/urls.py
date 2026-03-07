from django.urls import path
from .views import get_tasks,post_tasks,update_tasks


urlpatterns = [

  path('tasks/',get_tasks),
  path('tasks/create',post_tasks),
  path('tasks/update/<int:id>/',update_tasks),
]