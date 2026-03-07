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

@api_view(['POST'])

def post_tasks(request):
  serializer = TaskSerializer(data = request.data)
  
  if serializer.is_valid():
    serializer.save()

    return Response({"messege" : "Task Create Chesan ra Babu"})
  return serializer.errors

@api_view(['PATCH'])

def update_tasks(request,id):
  
  try:
    task = Task.objects.get(id=id)
  except:
    return Response({"error" : "Data Kanipinchatle ra babu"})
  
  serializer = TaskSerializer(task,data = request.data,partial = True)

  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data)
  
  return Response(serializer.errors )



def home(request):
  return HttpResponse("Server Backend Working Successfullyyy ! Hurrahhh")

def testt(request):
  return HttpResponse("Just Testing")

