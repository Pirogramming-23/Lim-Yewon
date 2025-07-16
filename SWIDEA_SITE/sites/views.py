from django.shortcuts import render, redirect
from .models import Idea

# Create your views here.
def views_main(request) :
    sort = request.GET.get('sort', 'title')
    
    sort_list = {
        "title" : "이름 오름차순",
        "-title" : "제목 내림차순",
        "created_at" : "최신순",
        "-created_at" : "등록순",
    }

    if sort not in sort_list:
        sort = 'title' 

    ideas = Idea.objects.all()

    ideas = ideas.order_by(sort)
    sort_text = sort_list[sort]

    context = {
        "ideas" : ideas,
        "sort" : sort_text,
    }
    return render(request, "main.html", context)

def ideas_read(request, pk) :
  ideas = Idea.objects.get(id=pk)
  context = {
    "ideas" : ideas
  }
  return render(request, "ideas_read.html", context)

def ideas_create(request) :
    devtools = Idea._meta.get_field('devtool').choices

    if request.method == "POST" :
        Idea.objects.create(
            title = request.POST["title"],
            photo = request.FILES["photo"],
            interest = request.POST["interest"],
            devtool = request.POST["devtool"],
            content = request.POST["content"],
        )
        return redirect("/")
    return render(request, "ideas_create.html", {
        "devtools": devtools
    })

def ideas_delete(request, pk) :
    if request.method == "POST" :
        idea = Idea.objects.get(id=pk)
        idea.delete()
    return redirect("/")

def ideas_update(request, pk) :
    idea = Idea.objects.get(id=pk)
    devtools = Idea._meta.get_field('devtool').choices

    if request.method == "POST" :
        if "photo" in request.FILES:
            idea.photo = request.FILES["photo"]

        idea.title = request.POST["title"]
        idea.interest = request.POST["interest"]
        idea.devtool = request.POST["devtool"]
        idea.content = request.POST["content"]
        idea.save()
        return redirect(f"/{pk}")
    context = {"idea" : idea, "devtools": devtools}
    return render(request, "ideas_update.html", context)