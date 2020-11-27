from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Comment
from .forms import CommentForm

# Create your views here.

def blog(request):
    posts = Post.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    context = {
        'posts': posts,
        'categories': categories,
    }
    return render(request, 'blog/blog.html', context)

def blog_detail(request, pk):
    posts = Post.objects.all()
    categories = Category.objects.all()
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post).order_by("-created_on")
    form = CommentForm()
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form_save = Comment(
                author = form.cleaned_data['author'],
                body = form.cleaned_data['body'],
                post = post
            )
            form_save.save()
            return redirect('blog')
    
    context = {
        "post": post, 
        "comments": comments, 
        "form": form, 
        'posts':posts,
        'categories': categories
        }
    return render(request, "blog/blog_detail.html", context)



def blog_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    categories = Category.objects.all()
    context = {
        'category': category,
        'categories': categories
    }
    return render(request, 'blog/blog_category.html', context)
