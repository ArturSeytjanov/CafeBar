from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from .models import Post
from .models import Comment
from .forms import CommentForm
from .forms import PostForm

def homePage(request):
    return render(request, 'post/home.html')

def aboutPage(request):
    #SQL -> SELECT * FROM Post;
    #SQL -> SELECT * FROM Post WHERE id = 1;
    posts = Post.objects.all()
    #text = Post.objects.get(id=1)
    context = {
        'posts': posts
    }
    return render(request, 'post/about.html', context)

def aboutDetail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = Comment.objects.all()
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment
            new_comment.save()
    else:
        comment_form = CommentForm()
    """try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        return render(request, 'post/404.html')"""
        
    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    }
    return render(request, 'post/about_detail.html', context)

def servicesPage(request):
    return render(request, 'post/services.html')

def contactPage(request):
    return render(request, 'post/contact.html')

def newPostPage(request):

    if request.method == 'POST':
        
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():    
            form.save()
            return HttpResponseRedirect(redirect_to='/about/')
    else:
        form = PostForm()
    
    context = {
        'form': form
    }
    return render(request=request, template_name='post/newpost.html', context=context)
