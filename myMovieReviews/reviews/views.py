from django.shortcuts import render, HttpResponse
from .models import Review

# Create your views here.
def reviews_list(request) :
    reviews = Review.objects.all()
    context = {
        "reviews" : reviews
    }
    return render(request, "reviews_list.html", context)

def reviews_read(request, pk) :
    review = Review.objects.get(id=pk)
    context = {
        "review" : review
    }
    return render(request, "reviews_read.html", context)