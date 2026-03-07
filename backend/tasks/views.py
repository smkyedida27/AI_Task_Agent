from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse

from .models import Task 
from .serializers import TaskSerializer
from .ai_parser import parse_content



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
  return Response(serializer.errors)


@api_view(['POST'])

def ai_command(request):

  text = request.data.get("text")

  result =  parse_content(text)
  return Response(result)


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
  
  return Response(serializer.errors)

@api_view(['DELETE'])

def delete_task(request,id):
  try:
    task = Task.objects.get(id=id)
  except:
    return Response({"messege" : "Delete avaledhu ra babu sariga delete chey"})
  task.delete()
  return Response({"messege" : "Delete ayindhi le"})




def home(request):
  return HttpResponse("Server Backend Working Successfullyyy ! Hurrahhh")

def testt(request):
  return HttpResponse("Just Testing")

