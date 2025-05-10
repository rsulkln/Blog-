from django.contrib import admin
from .models import Blog

class PostList(admin.ModelAdmin):
    list_display = (
        'TITLE',
        'AUTHOR',
        "BODY",
    )

admin.site.register(Blog,PostList)
