from django.shortcuts import render, redirect, get_object_or_404
from .models import DevTool
from sites.models import Idea

# Create your views here.
def devtools_list(request) :
    devtools = DevTool.objects.all()

    context = {
        "devtools" : devtools,
    }
    return render(request, "devtools_list.html", context)

def devtools_read(request, pk) :
    devtools = DevTool.objects.get(id=pk)
    context = {
        "devtools" : devtools
    }
    return render(request, "devtools_read.html", context)

def devtools_create(request) :
    devtools = DevTool.objects.all()

    if request.method == "POST" :
        DevTool.objects.create(
            name = request.POST["name"],
            kind = request.POST["kind"],
            content = request.POST["content"],
        )
        return redirect("/devtools/")
    return render(request, "devtools_create.html", {
        "devtools": devtools
    })

def devtools_delete(request, pk) :
    if request.method == "POST" :
        idea = DevTool.objects.get(id=pk)
        idea.delete()
    return redirect("/devtools/")

def devtools_update(request, pk) :
    devtools = DevTool.objects.get(id=pk)

    if request.method == "POST" :
        devtools.name = request.POST["name"]
        devtools.kind = request.POST["kind"]
        devtools.content = request.POST["content"]
        devtools.save()
        return redirect(f"/devtools/{pk}")
    context = {"devtool" : devtools}
    return render(request, "devtools_update.html", context)

def devtool_detail(request, pk):
    devtool = get_object_or_404(DevTool, pk=pk)
    ideas = Idea.objects.filter(devtool=devtool)

    context = {
        'devtool': devtool,
        'ideas': ideas
    }
    return render(request, 'devtools/devtools_read.html', context)