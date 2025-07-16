from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Idea, IdeaStar
from devtools.models import DevTool
from django.http import JsonResponse
from django.views.decorators.http import require_POST

# Create your views here.
def views_main(request) :
    sort = request.GET.get('sort', 'title')
    
    sort_list = {
        "title" : "이름 오름차순",
        "-title" : "제목 내림차순",
        "created_at" : "등록순",
        "-created_at" : "최신순",
    }

    if sort not in sort_list:
        sort = 'title' 

    ideas = Idea.objects.all()

    user_stars = []
    if request.user.is_authenticated:
        user_stars = IdeaStar.objects.filter(user=request.user).values_list('item_id', flat=True)


    ideas = ideas.order_by(sort)
    sort_text = sort_list[sort]

    context = {
        "ideas" : ideas,
        "sort" : sort_text,
        "user_stars" : user_stars
    }
    return render(request, "main.html", context)

def ideas_read(request, pk) :
  ideas = Idea.objects.get(id=pk)
  context = {
    "ideas" : ideas
  }
  return render(request, "ideas_read.html", context)

def ideas_create(request) :
    devtools = DevTool.objects.all()

    if request.method == "POST":
        devtool_obj = DevTool.objects.get(id=int(request.POST["devtool"]))

        Idea.objects.create(
            title = request.POST["title"],
            photo = request.FILES.get("photo"),
            interest = request.POST["interest"],
            devtool = devtool_obj,
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

def ideas_update(request, pk):
    idea = Idea.objects.get(id=pk)
    devtools = DevTool.objects.all()

    if request.method == "POST":
        if "photo" in request.FILES:
            idea.photo = request.FILES["photo"]

        idea.title = request.POST.get("title")
        idea.interest = request.POST.get("interest")
        idea.content = request.POST.get("content")

        devtool_id = request.POST.get("devtool")
        if devtool_id:
            idea.devtool = DevTool.objects.get(id=int(devtool_id))

        idea.save()
        return redirect(f"/{pk}")
    
    context = {
        "idea": idea,
        "devtools": devtools,
    }
    return render(request, "ideas_update.html", context)

@login_required
def toggle_star(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    user = request.user

    star, created = IdeaStar.objects.get_or_create(user=user, item=idea)
    if not created:
        # 이미 찜한 상태면 취소
        star.delete()

    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
@require_POST
def change_interest(request, pk, action):
    idea = Idea.objects.get(pk=pk)

    if action == 'plus':
        idea.interest += 1
    elif action == 'minus':
        if idea.interest > 0:
            idea.interest -= 1
    idea.save()

    return JsonResponse({'interest': idea.interest})