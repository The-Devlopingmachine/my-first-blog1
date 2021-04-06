from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
# Create your views here.

def post_list(request):

    # Passing the posts we have so far created
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    
    return render(request, 'blog/post_list.html', {"posts": posts})

def post_new(request):

    # Taking the data input from the 
    if request.method == "POST":
        
        # Taking the form from the post method
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)

    else:
        form = PostForm()

    return render(request, 'blog/new_post.html', {"form": form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk = pk)
    return render(request, 'blog/post_detail.html', {'post': post} )