from django.shortcuts import render, get_object_or_404
from .models import Blog
 

def post_list(request):
    post = Blog.objects.all()
    return render(request,"home.html",{"post":post})

def post_detail(request,pk):
    post = get_object_or_404(Blog,pk = pk )
    return render (request,"post_detail.html",{"post":post})
