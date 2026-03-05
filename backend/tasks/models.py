from django.db import models
from django.contrib.auth.models import User
class Task(models.Model):
  task_text = models.TextField()

  status = models.CharField(
    max_length = 20,default= "pending"
  )
  created_at = models.DateTimeField(auto_now_add=True)

  user = models.ForeignKey(
    User,on_delete=models.CASCADE)
  
  def __str__(self):
    return self.task_text


