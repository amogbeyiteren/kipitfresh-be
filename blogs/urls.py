from django.urls import path
from .views import BlogListCreateView, BlogDetailView, MakeFeaturedStoryView, LoginView, FeaturedBlogsListView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('blogs/', BlogListCreateView.as_view(), name='blog-list-create'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('blogs/<int:pk>/make-featured/', MakeFeaturedStoryView.as_view(), name='make-featured'),
    path('blogs/featured/', FeaturedBlogsListView.as_view(), name='featured-blogs-list'),
]
