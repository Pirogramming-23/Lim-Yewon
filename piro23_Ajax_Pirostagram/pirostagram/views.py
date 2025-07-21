from django.shortcuts import render, redirect
from .models import Post, Comment
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

# Create your views here.
def posts_list(request) :
    posts = Post.objects.all()
    context = {
        'posts' : posts,
    }
    return render(request, 'posts/posts_list.html', context)

def posts_detail(request, pk) :
    post = Post.objects.get(id=pk)
    comments = Comment.objects.filter(post=post)
    context = {
        "post" : post,
        "comments" : comments,
    }
    return render(request, "posts/posts_detail.html", context)

@csrf_exempt
def like_ajax(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        post_id = data.get('id')

        post = Post.objects.get(id=post_id)
        post.like += 1
        post.save()

        return JsonResponse({'id': post.id, 'like': post.like})
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def comments_create(request, post_id):
    Comment.objects.create(post_id=post_id, content=request.POST["content"])
    return redirect(f"/{post_id}/")

def delete_comment(request, comment_id):
    if request.method == "POST":
        try:
            comment = Comment.objects.get(id=comment_id)
            comment.delete()
            return JsonResponse({'status': 'success'})
        except Comment.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Comment not found'}, status=404)
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)