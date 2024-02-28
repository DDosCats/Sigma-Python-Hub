from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required

def index(request):
    
    posts = Post.objects.filter(is_published=True)
    create_form = PostForm()
    
    context = {
        'posts': posts,
        'form': create_form
    }
    
    return render(request, 'blog/index.html', context)

@login_required
def post(request, post_id):
    form_comment = CommentForm()
    post = get_object_or_404(Post, id=post_id)
    post.views += 1
    post.save()
    context = {
        'post': post,
        'comment_form': form_comment,
    }
    
    return render(request, 'blog/post.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return redirect('blog:index')

@login_required
def comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            print(comment)
            comment.post = post
            comment.author = request.user
            comment.save()
    return redirect('blog:post', post_id=post_id)

@login_required
def like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    post.save()
    return JsonResponse({'likes': post.likes.count()})


@login_required
def dislike(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.likes.all():
        post.dislike.remove(request.user)
    else:   
        post.dislike.add(request.user)
    post.save()
    return JsonResponse({'dislikes': post.dislike.count()})

@login_required
def like_comment(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, post__id=post_id)
    if request.user in comment.likes.all():
        comment.likes.remove(request.user)
    else:
        comment.likes.add(request.user)
    comment.save()
    return JsonResponse({'likes': comment.likes.count()})