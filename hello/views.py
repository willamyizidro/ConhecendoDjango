from django.shortcuts import render
from django.utils.timezone import datetime
from django.http import HttpResponse
import re

def home(request):
    return HttpResponse("hello asdas   é django! ")

def hello_there(request, name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")
    

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now +" willamy"
    return HttpResponse(content)

print("http://127.0.0.1:8000/hello/VSCode")
# Create your views here.
