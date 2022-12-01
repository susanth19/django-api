from django.shortcuts import render
from django.http import HttpResponse
from bson import ObjectId

# Create your views here.
from demoapp.models import Todo
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def add_post(request):
    # comment=request.POST.get("comment").split(",")
    # tags=request.POST.get("tags").split(",")
    # user_details={"first_name":request.POST.get("first_name"),"last_name":request.POST.get("last_name")}
    post=Todo(first_name=request.POST.get("first_name"),last_name=request.POST.get("last_name"))
    post.save()
    return HttpResponse("Inserted")

@csrf_exempt
def update_post(request,id):
    post=Todo.objects.get(id=id)
    post.first_name=request.POST.get('first_name')
    post.save()
    return HttpResponse("Post Updated")

def read_post(request,id):
    post=Todo.objects.get(id=id)
    stringval="First Name : "+post.first_name+" Last name : "+post.last_name
    return HttpResponse(stringval)

def read_post_all(request):
    posts=Todo.objects.all()
    stringval=""
    for post in posts:
        stringval += "First Name : " + post.first_name + " Last name : " + post.last_name
    #    print(end="")

    return HttpResponse(stringval)

def delete_post(request,id):
    post=Todo.objects.get(id=id)
    post.delete()
    return HttpResponse("Post Deleted")
