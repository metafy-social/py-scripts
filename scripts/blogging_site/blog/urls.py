from blog.models import Post
from django.urls import path
from . import views
from .views import CommentCreateView, PostListView,PostDetailView, PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', PostListView.as_view(),name="blog-home"),
    path('user/<str:username>', UserPostListView.as_view(),name="user-posts"),
    path('post/<int:pk>/', PostDetailView.as_view(),name="post-detail"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(),name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(),name="post-delete"),
    path('post/<int:pk>/comment', CommentCreateView.as_view(),name="comment-new"),
    path('like/<int:pk>',views.LikeView,name='like_post'),
    path('post/new/', PostCreateView.as_view(),name="post-create"),
    path('about/', views.about,name="blog-about"),
    path('search/', views.SearchView,name="blog-search"),
    path('collegestudds/', views.collegestuddes,name="blog-college"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)