from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from .forms import PostForm
from .models import Post

@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, "Post created successfully!")
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated successfully!")
            return redirect('profile')
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/edit_post.html', {'form': form, 'post': post})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    if request.method == "POST":
        post.delete()
        messages.success(request, "Post deleted successfully!")
        return redirect('profile')
    return render(request, 'posts/delete_post.html', {'post': post})

def home(request):
    posts = Post.objects.all()

    date_filter = request.GET.get('date', 'latest')
    if date_filter == 'oldest':
        posts = posts.order_by('created_at')
    else:
        posts = posts.order_by('-created_at')

    media_type = request.GET.get('media_type')
    if media_type == 'text':
        posts = posts.filter(Q(image__isnull=True) | Q(image=''))
    elif media_type == 'image':
        posts = posts.exclude(Q(image__isnull=True) | Q(image=''))

    author = request.GET.get('author')
    if author:
        posts = posts.filter(user__username=author)

    search_query = request.GET.get('search')
    if search_query:
        posts = posts.filter(Q(content__icontains=search_query))

    return render(request, 'posts/home.html', {'posts': posts})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'posts/register.html', {'form': form})

@login_required
def profile(request):
    user_posts = Post.objects.filter(user=request.user)
    return render(request, 'posts/profile.html', {'posts': user_posts})