from django.shortcuts import render
from blog.models import BlogPost,Blogger,Comment
from django.views import generic
from django.shortcuts import get_object_or_404

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