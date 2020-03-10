from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish', 'created', 'status',)
    search_fields = ('author', 'title', 'publish',)
    prepopulated_fields = {"slug": ("title",)}
