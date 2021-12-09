from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def main(request):
    return render(request, 'test1/index.html')

def CS(request):
    return render(request, 'test1/CS.html')

def star(request):
    return render(request, 'test1/star.html')

def IT(request):
    return render(request, 'test1/IT.html')

def EEE(request):
    return render(request, 'test1/EEE.html')

    
def EC(request):
    return render(request, 'test1/EC.html')

def MECH(request):
    return render(request, 'test1/MECH.html')