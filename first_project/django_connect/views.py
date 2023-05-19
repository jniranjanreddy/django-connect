from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dict = {'insert_content':"Hello I am from django_connect"}
    return render(request,'django_connect/index.html',context=my_dict)