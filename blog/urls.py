from django.urls import path
from .views import BlogDetailView
from . views import BlogListView
from . views import BlogCreateView
from . views import BlogUpdateView
from . views import BlogDeleteView


urlpatterns = [
    path("post/<int:pk>/",BlogDetailView.as_view(),name="post_detail"),
    path("",BlogListView.as_view(),name="home"),
    path("post/new/",BlogCreateView.as_view(),name="Blog_new"),
    path('post/<int:pk>/edit/',BlogUpdateView.as_view(),name="post_edit"),
    path('post/<int:pk>/delete/',BlogDeleteView.as_view(),name="post_delete"),
]


