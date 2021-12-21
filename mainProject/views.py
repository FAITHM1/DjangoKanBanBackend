from django.shortcuts import render
##for sendinf json response
from django.http import JsonResponse
##to turn json string into dictionaries
import json
## To serialize objects into json strings
from django.core.serializers import serialize
##project model
from .models import SubProject,MainProject
##view clas
from django.views import View
## GetBody
from .helpers import GetBody
from .models import SubProject,MainProject
# Create your views here.
class ProjectView(View):
  def get(self,request):
    all = MainProject.objects.all()
    serialized = serialize("json",all)
    finalData = json.loads(serialized)
    return JsonResponse(finalData, safe=False)
  
  def post (self,request):
    ##get data from body
    body = GetBody(request)
    ## create new project
    project = MainProject.objects.create(title = body["title"],type = body["type"])
    finalData = json.loads(serialize("json",[project]))
    return JsonResponse(finalData, safe=False)
  
class ProjectViewId(View):
  def get(self, request,id):
    project = MainProject.objects.get(id=id)
    finalData=json.loads(serialize("json",[project]))
    return JsonResponse(finalData, safe=False)
  
  def put (self, request, id):
    body = GetBody(request)
    # ** is the js spread operator 
    MainProject.objects.filter(id=id).update(**body)
    project = MainProject.objects.get(id=id)
    finalData=json.loads(serialize("json",[project]))
    return JsonResponse(finalData, safe=False)
    
  def delete (self, request,id):
    project = MainProject.objects.get(id=id)
    project.delete()
    finalData=json.loads(serialize("json",[project]))
    return JsonResponse(finalData, safe=False)
 
class SubProjectView(View):
  def get(self,request):
    all = SubProject.objects.all()
    serialized = serialize("json",all)
    finalData = json.loads(serialized)
    return JsonResponse(finalData, safe=False)
  def post (self,request):
    ##get data from body
    body = GetBody(request)
    ## create new project
    project = SubProject.objects.create(name = body["name"],description = body["description"],workingOn = body["workingOn"],mainProjectnum = body["mainProjectnum"])
    finalData = json.loads(serialize("json",[project]))
    return JsonResponse(finalData, safe=False)
  
  
class SubProjectViewId(View):
  def get(self, request,id):
    project = SubProject.objects.get(id=id)
    finalData=json.loads(serialize("json",[project]))
    return JsonResponse(finalData, safe=False)
  
  def put (self, request, id):
    body = GetBody(request)
    # ** is the js spread operator 
    SubProject.objects.filter(id=id).update(**body)
    project = SubProject.objects.get(id=id)
    finalData=json.loads(serialize("json",[project]))
    return JsonResponse(finalData, safe=False)
    
  def delete (self, request,id):
    project = SubProject.objects.get(id=id)
    project.delete()
    finalData=json.loads(serialize("json",[project]))
    return JsonResponse(finalData, safe=False)