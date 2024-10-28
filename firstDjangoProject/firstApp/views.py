import json

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from firstApp.models import BookModel


# Create your views here.
def home(request):
    return render(request, "firstApp/index.html")

def about(request):
    return HttpResponse("This is about page of the first app")


def all_books(request):
    # getting all the books
    books = BookModel.objects.all()

    # prepare the result
    context = {"books": books}
    return render(request, "firstApp/index.html", context)


def book_detail(request, book_id):
    book =get_object_or_404(BookModel, pk=book_id)
    return render(request, "firstApp/book_detail.html", {"book": book})
