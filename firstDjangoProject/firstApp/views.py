from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "firstApp/index.html")

def about(request):
    return HttpResponse("This is about page of the first app")
