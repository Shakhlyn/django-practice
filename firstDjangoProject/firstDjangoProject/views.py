from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse("This is home page")

def about(request):
    # return HttpResponse("This is about page")
    return render(request, 'index.html')
