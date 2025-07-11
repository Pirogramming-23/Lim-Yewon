from django.shortcuts import render, redirect
from .models import Review

# Create your views here.
def reviews_list(request) :
    sort = request.GET.get('sort', 'title')
    
    sort_list = {
        "title" : "제목 오름차순",
        "-title" : "제목 내림차순",
        "rating" : "별점 낮은 순",
        "-rating" : "별점 높은 순",
        "year" : "개봉년도 오름차순",
        "-year" : "개봉년도 내림차순",
        "running_time" : "러닝타임 낮은 순",
        "-running_time" : "러닝타임 높은 순"
    }

    if sort not in sort_list:
        sort = 'title' 

    search = request.GET.get('search')
    reviews = Review.objects.all()

    if search:
        from django.db.models import Q
        reviews = reviews.filter(
            Q(title__icontains=search) | Q(director__icontains=search)
        )

    reviews = reviews.order_by(sort)
    sort_text = sort_list[sort]
    context = {
        "reviews" : reviews,
        "sort" : sort_text,
        "search" : search,
    }
    return render(request, "reviews_list.html", context)

def reviews_read(request, pk) :
    review = Review.objects.get(id=pk)
    running_time = review.running_time or 0
    hours = running_time // 60
    minutes = running_time % 60

    if hours and minutes:
        printed_time = f"{hours}시간 {minutes}분"
    elif hours:
        printed_time = f"{hours}시간"
    else:
        printed_time = f"{minutes}분"

    context = {
        "review" : review,
        "printed_time": printed_time
    }
    return render(request, "reviews_read.html", context)

def reviews_create(request) :
    genre_choices = Review._meta.get_field('genre').choices

    if request.method == "POST" :
        Review.objects.create(
            poster = request.FILES["poster"],
            title = request.POST["title"],
            year = request.POST["year"],
            director = request.POST["director"],
            actors = request.POST["actors"],
            genre = request.POST["genre"],
            rating = request.POST["rating"],
            running_time = request.POST["running_time"],
            content = request.POST["content"],
        )
        return redirect("/reviews/")
    return render(request, "reviews_create.html", {
        "genre_choices": genre_choices
    })

def reviews_delete(request, pk) :
    if request.method == "POST" :
        review = Review.objects.get(id=pk)
        review.delete()
    return redirect("/reviews/")

def reviews_update(request, pk) :
    review = Review.objects.get(id=pk)
    genre_choices = Review._meta.get_field('genre').choices

    if request.method == "POST" :
        if "poster" in request.FILES:
            review.poster = request.FILES["poster"]
        review.title = request.POST["title"]
        review.year = request.POST["year"]
        review.director = request.POST["director"]
        review.actors = request.POST["actors"]
        review.genre = request.POST["genre"]
        review.rating = request.POST["rating"]
        review.running_time = request.POST["running_time"]
        review.content = request.POST["content"]
        review.save()
        return redirect(f"/reviews/{pk}")
    context = {"review" : review, "genre_choices": genre_choices}
    return render(request, "reviews_update.html", context)