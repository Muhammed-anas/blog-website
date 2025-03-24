from django.contrib import admin
from .models import posts
# Register your models here.


class PostsAdmin(admin.ModelAdmin):
    pass

admin.site.register(posts,PostsAdmin)