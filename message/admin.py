from django.contrib import admin
from .models import Mes, Post
from .forms import *

admin.site.register(Mes)
admin.site.register(Post)


class AdminPosts(admin.ModelAdmin):
    list_display = ('title', 'content', 'photo')
# Register your models here.
