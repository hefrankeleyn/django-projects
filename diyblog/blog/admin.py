from django.contrib import admin
from blog.models import BlogPost,Blogger,Comment
# Register your models here.

#admin.site.register(BlogPost)
#admin.site.register(Blogger)
#admin.site.register(Comment)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','blogger','postDate')

@admin.register(Blogger)
class BloggerAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','sex','age','profession')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('commenter','comment_datetime','blogPost')