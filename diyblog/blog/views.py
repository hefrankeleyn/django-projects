from django.shortcuts import render
from blog.models import BlogPost,Blogger,Comment
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    """ View function for home page of site. """
    
    # Generate counts of some of the main objects
    num_blogPost = BlogPost.objects.all().count()
    num_blogger = Blogger.objects.all().count()
  
    context = {
        'num_blogPost':num_blogPost,
        'num_blogger':num_blogger,
    }
    
    # Render the HTML templete index.html with the data in the context variable
    return render(request,'index.html',context)

# BlogPost list
class BlogPostListView(generic.ListView):
    model = BlogPost
    def get_queryset(self):
        return BlogPost.objects.all()

class BlogPostDetailView(generic.DetailView):
    model = BlogPost

class BloggerListView(generic.ListView):
    model = Blogger
    def get_queryset(self):
        return Blogger.objects.all()

class BloggerDetailViews(generic.DetailView):
    model = Blogger

from django.views.generic.edit import CreateView
from blog.forms import CommentFormat
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect

@login_required
def create_comment(request):
    comment_format = CommentFormat(request.POST)
    comment = Comment()
    if comment_format.is_valid():
        comment.content = comment_format.cleaned_data['content']
        blogpost_id = comment_format.cleaned_data['blogpost_id']
        blogpost = get_object_or_404(BlogPost,pk=blogpost_id)
        comment.blogPost = blogpost
        #user = request.session['user']
        #comment.user = user
        comment.save()
        return redirect('blogPost-detail',pk=blogpost_id)


@login_required
def create_comment_view(request,pk):
    """ get user by pk"""
    blogpost = get_object_or_404(BlogPost,pk=pk)
    return render(request,'blog/create_comment.html',{'blogpost':blogpost})