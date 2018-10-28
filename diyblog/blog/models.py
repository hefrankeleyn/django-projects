from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class BlogPost(models.Model):
    # title of blog
    title = models.CharField(max_length=100,help_text='Enter post title')
    # author of blogger, one blog to one author
    blogger = models.ForeignKey('Blogger',models.SET_NULL,null=True,blank=True)
    #user = models.ForeignKey('User',on_delete=models.SET_NULL,null=True,blank=True)
    # datetime of blog by worte
    postDate = models.DateTimeField(auto_now=True)
    # content of blog
    content = models.TextField(max_length=20000,help_text='Enter your content of blog.')
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blogPost-detail',args=[str(self.id)])
    
class Blogger(models.Model):
    first_name=models.CharField(max_length=50,help_text='Please enter first name.')
    last_name=models.CharField(max_length=50,help_text='Please enter last name.')
    SEX_STATUS=((0,'male'),(1,'female'))
    sex=models.IntegerField(
        null=True,
        choices=SEX_STATUS,
        default=0,
        help_text='Please enter male or female',
    )
    age=models.IntegerField(
        null=True,
        help_text='Please enter age witch is between 0 and 120.'
    )
    profession=models.CharField(
        max_length=30,
        blank=True,
        help_text='Please enter your profession.'
    )
    
    def __str__(self):
        return f'{self.first_name},{self.last_name}'
    
    def get_absolute_url(self):
        return reverse('blogger-detail',args=[str(self.id)])

class Comment(models.Model):
    commenter = models.ForeignKey('Blogger',models.SET_NULL,null=True,blank=True)
    content = models.TextField(max_length=300,help_text='Please enter your comment')
    comment_datetime = models.DateTimeField(auto_now_add=True)
    #user = models.ForeignKey('User',on_delete=models.SET_NULL,null=True,blank=True)
    blogPost = models.ForeignKey(BlogPost,models.SET_NULL,null=True,blank=True)
    
    class Meta:
        ordering = ['-comment_datetime']
    def __str__(self):
        return f'{self.id},{self.blogPost.title}'
