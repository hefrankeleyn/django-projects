from django.urls import path
from blog import views

urlpatterns = [
    path('',views.index,name='index'),
    path('blogPosts/',views.BlogPostListView.as_view(),name='blogPosts'),
    path('blogPost/<int:pk>/',views.BlogPostDetailView.as_view(),name='blogPost-detail'),
    path('bloggers/',views.BloggerListView.as_view(),name='bloggers'),
    path('blogger/<int:pk>',views.BloggerDetailViews.as_view(),name='blogger-detail')
]