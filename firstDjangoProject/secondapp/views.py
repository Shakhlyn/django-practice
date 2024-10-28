from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'secondapp/index.html')

def about(request):
    return HttpResponse("This is the About Page of the second app")
