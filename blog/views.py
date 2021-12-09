from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.
def blogs(request):
    return render(request,'index.html')