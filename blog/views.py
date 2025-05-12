from django.views.generic import ListView, DetailView
from .models import Blog
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

class BlogListView(ListView):
    model = Blog 
    template_name = "home.html"


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog_detail.html"

class BlogCreateView(CreateView):
    model = Blog 
    fields = ['TITLE','AUTHOR','BODY']
    template_name = "blog_form.html"
    success_url = reverse_lazy("home")

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['TITLE','BODY']
    template_name = "blog_edit_form.html"
    success_url = reverse_lazy("home")

class BlogDeleteView(DeleteView):
    model = Blog 
    template_name = "blog_delete.html"
    success_url = reverse_lazy("home")
