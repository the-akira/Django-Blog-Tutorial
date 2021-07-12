from django.contrib import admin
from django.urls import path
from blog.views import PostListView, PostDetailView
from blog import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-index'),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('search/', views.search, name='search'),
    path('admin/', admin.site.urls),
]