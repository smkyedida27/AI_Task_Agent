from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse

from .models import Task 
from .serializers import TaskSerializer

@api_view(['GET'])

def get_tasks(request):
  tasks = Task.objects.all()

  serializer = TaskSerializer(tasks,many=True)

  return Response(serializer.data)


def home(request):
  return HttpResponse("Server Backend Working Successfullyyy ! Hurrahhh")

